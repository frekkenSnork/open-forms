from datetime import datetime
from decimal import Decimal

from django.core import mail
from django.test import TestCase, override_settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from freezegun import freeze_time

from openforms.config.models import GlobalConfiguration
from openforms.forms.tests.factories import (
    FormDefinitionFactory,
    FormFactory,
    FormStepFactory,
)
from openforms.submissions.exports import create_submission_export
from openforms.submissions.models import Submission
from openforms.submissions.tests.factories import (
    SubmissionFactory,
    SubmissionFileAttachmentFactory,
    SubmissionReportFactory,
    SubmissionStepFactory,
)
from openforms.utils.tests.html_assert import HTMLAssertMixin

from ....service import NoSubmissionReference, extract_submission_reference
from ..constants import AttachmentFormat
from ..plugin import EmailRegistration


@override_settings(DEFAULT_FROM_EMAIL="info@open-forms.nl")
class EmailBackendTests(HTMLAssertMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form = FormFactory.create(
            name="MyName", internal_name="MyInternalName", registration_backend="email"
        )
        cls.fd = FormDefinitionFactory.create()
        cls.fs = FormStepFactory.create(form=cls.form, form_definition=cls.fd)

    def test_submission_with_email_backend(self):
        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
        )

        data = {"foo": "bar", "some_list": ["value1", "value2"]}

        submission = SubmissionFactory.create(form=self.form)
        submission_step = SubmissionStepFactory.create(
            submission=submission, form_step=self.fs, data=data
        )
        submission.completed_on = timezone.make_aware(datetime(2021, 1, 1, 12, 0, 0))
        submission.save()

        SubmissionFileAttachmentFactory.create(
            submission_step=submission_step,
            file_name="my-foo.bin",
            content_type="application/foo",
        )
        SubmissionFileAttachmentFactory.create(
            submission_step=submission_step,
            file_name="my-bar.txt",
            content_type="text/bar",
        )

        email_submission = EmailRegistration("email")
        email_submission.register_submission(submission, email_form_options)

        # Verify that email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Verify we've generated a public_registration_reference
        self.assertNotEqual(submission.public_registration_reference, "")

        message = mail.outbox[0]
        self.assertEqual(
            message.subject,
            _("[Open Forms] {form_name} - submission {public_reference}").format(
                form_name=submission.form.admin_name,
                public_reference=submission.public_registration_reference,
            ),
        )
        self.assertEqual(message.from_email, "info@open-forms.nl")
        self.assertEqual(message.to, ["foo@bar.nl", "bar@foo.nl"])

        # Check that the template is used
        message_html = message.alternatives[0][0]
        self.assertHTMLValid(message_html)
        self.assertIn("<table", message_html)
        self.assertNotIn("<table", message.body)

        self.assertIn(
            _("Submission details for %(form_name)s (submitted on %(datetime)s)")
            % dict(form_name=self.form.admin_name, datetime="12:00:00 01-01-2021"),
            message_html,
        )
        self.assertIn(
            _("Submission details for %(form_name)s (submitted on %(datetime)s)")
            % dict(form_name=self.form.admin_name, datetime="12:00:00 01-01-2021"),
            message.body,
        )

        self.assertIn("foo: bar", message.body)
        self.assertIn("some_list: value1, value2", message.body)

        self.assertTagWithTextIn("td", "foo", message_html)
        self.assertTagWithTextIn("td", "bar", message_html)
        self.assertTagWithTextIn("td", "some_list", message_html)
        self.assertTagWithTextIn("td", "value1, value2", message_html)

        self.assertEqual(len(message.attachments), 2)
        file1, file2 = message.attachments
        self.assertEqual(file1[0], "my-foo.bin")
        self.assertEqual(file1[1], b"content")  # still bytes
        self.assertEqual(file1[2], "application/foo")

        self.assertEqual(file2[0], "my-bar.txt")
        self.assertEqual(file2[1], "content")  # this is text now
        self.assertEqual(file2[2], "text/bar")

    def test_submission_with_email_backend_strip_out_urls(self):
        config = GlobalConfiguration.get_solo()
        config.email_template_netloc_allowlist = []
        config.save()

        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
        )

        data = {
            "foo": "https://someurl.com",
        }

        submission = SubmissionFactory.create(form=self.form)
        SubmissionStepFactory.create(
            submission=submission, form_step=self.fs, data=data
        )
        submission.completed_on = timezone.make_aware(datetime(2021, 1, 1, 12, 0, 0))
        submission.save()

        email_submission = EmailRegistration("email")
        email_submission.register_submission(submission, email_form_options)

        # Verify that email was sent
        self.assertEqual(len(mail.outbox), 1)

        message = mail.outbox[0]
        message_html = message.alternatives[0][0]

        self.assertNotIn("https://someurl.com", message.body)
        self.assertNotIn("https://someurl.com", message_html)

    def test_submission_with_email_backend_keep_allowed_urls(self):
        config = GlobalConfiguration.get_solo()
        config.email_template_netloc_allowlist = ["allowed.com"]
        config.save()

        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
        )

        data = {
            "foo": "https://allowed.com",
        }

        submission = SubmissionFactory.create(form=self.form)
        SubmissionStepFactory.create(
            submission=submission, form_step=self.fs, data=data
        )
        submission.completed_on = timezone.make_aware(datetime(2021, 1, 1, 12, 0, 0))
        submission.save()

        email_submission = EmailRegistration("email")
        email_submission.register_submission(submission, email_form_options)

        # Verify that email was sent
        self.assertEqual(len(mail.outbox), 1)

        message = mail.outbox[0]
        message_html = message.alternatives[0][0]

        self.assertIn("https://allowed.com", message.body)
        self.assertIn("https://allowed.com", message_html)

    @freeze_time("2021-01-01 10:00")
    def test_register_and_update_paid_product(self):
        submission = SubmissionFactory.from_data(
            {"voornaam": "Foo"},
            form__product__price=Decimal("11.35"),
            form__payment_backend="demo",
            registration_success=True,
            public_registration_reference="XYZ",
        )
        self.assertTrue(submission.payment_required)

        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
        )
        email_submission = EmailRegistration("email")
        email_submission.update_payment_status(submission, email_form_options)

        # Verify that email was sent
        self.assertEqual(len(mail.outbox), 1)

        message = mail.outbox[0]
        self.assertEqual(
            message.subject,
            _(
                "[Open Forms] {form_name} - submission payment received {public_reference}"
            ).format(
                form_name=submission.form.admin_name,
                public_reference=submission.public_registration_reference,
            ),
        )
        self.assertEqual(message.from_email, "info@open-forms.nl")
        self.assertEqual(message.to, ["foo@bar.nl", "bar@foo.nl"])

    def test_no_reference_can_be_extracted(self):
        submission = SubmissionFactory.create(
            form=self.form,
            completed=True,
            registration_success=True,
            registration_result="irrelevant",
        )

        with self.assertRaises(NoSubmissionReference):
            extract_submission_reference(submission)

    @override_settings(DEFAULT_FROM_EMAIL="info@open-forms.nl")
    def test_submission_with_email_backend_export_csv_xlsx(self):
        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
            attachment_formats=[AttachmentFormat.csv, AttachmentFormat.xlsx],
        )

        data = {"foo": "bar", "some_list": ["value1", "value2"]}

        submission = SubmissionFactory.create(form=self.form)
        submission_step = SubmissionStepFactory.create(
            submission=submission, form_step=self.fs, data=data
        )
        submission.completed_on = timezone.make_aware(datetime(2021, 1, 1, 12, 0, 0))
        submission.save()

        SubmissionFileAttachmentFactory.create(
            submission_step=submission_step,
            file_name="my-foo.bin",
            content_type="application/foo",
        )
        SubmissionFileAttachmentFactory.create(
            submission_step=submission_step,
            file_name="my-bar.txt",
            content_type="text/bar",
        )

        email_submission = EmailRegistration("email")
        email_submission.register_submission(submission, email_form_options)

        # Verify that email was sent
        self.assertEqual(len(mail.outbox), 1)

        message = mail.outbox[0]

        # Two upload attachments and two export attachments
        self.assertEqual(len(message.attachments), 4)

        file1, file2, csv_export, xlsx_export = message.attachments
        self.assertEqual(file1[0], "my-foo.bin")
        self.assertEqual(file1[1], b"content")  # still bytes
        self.assertEqual(file1[2], "application/foo")

        self.assertEqual(file2[0], "my-bar.txt")
        self.assertEqual(file2[1], "content")  # this is text now
        self.assertEqual(file2[2], "text/bar")

        qs = Submission.objects.filter(pk=submission.pk)
        self.assertEqual(
            csv_export[0], f"{submission.form.admin_name} - submission.csv"
        )
        self.assertEqual(csv_export[1], create_submission_export(qs).export("csv"))
        self.assertEqual(csv_export[2], "text/csv")

        self.assertEqual(
            xlsx_export[0], f"{submission.form.admin_name} - submission.xlsx"
        )
        self.assertEqual(xlsx_export[1], create_submission_export(qs).export("xlsx"))
        self.assertEqual(
            xlsx_export[2],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    @override_settings(DEFAULT_FROM_EMAIL="info@open-forms.nl")
    def test_submission_with_email_backend_export_pdf(self):
        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
            attachment_formats=[AttachmentFormat.pdf],
        )

        data = {"foo": "bar", "some_list": ["value1", "value2"]}

        submission = SubmissionFactory.create(form=self.form)
        submission_step = SubmissionStepFactory.create(
            submission=submission, form_step=self.fs, data=data
        )
        submission.completed_on = timezone.make_aware(datetime(2021, 1, 1, 12, 0, 0))
        submission.save()

        report = SubmissionReportFactory.create(submission=submission)

        SubmissionFileAttachmentFactory.create(
            submission_step=submission_step,
            file_name="my-foo.bin",
            content_type="application/foo",
        )
        SubmissionFileAttachmentFactory.create(
            submission_step=submission_step,
            file_name="my-bar.txt",
            content_type="text/bar",
        )

        email_submission = EmailRegistration("email")
        email_submission.register_submission(submission, email_form_options)

        # Verify that email was sent
        self.assertEqual(len(mail.outbox), 1)

        message = mail.outbox[0]

        # Two upload attachments and one export attachment
        self.assertEqual(len(message.attachments), 3)

        file1, file2, pdf_export = message.attachments
        self.assertEqual(file1[0], "my-foo.bin")
        self.assertEqual(file1[1], b"content")  # still bytes
        self.assertEqual(file1[2], "application/foo")

        self.assertEqual(file2[0], "my-bar.txt")
        self.assertEqual(file2[1], "content")  # this is text now
        self.assertEqual(file2[2], "text/bar")

        self.assertEqual(pdf_export[0], f"{report.title}.pdf")
        self.assertEqual(pdf_export[1], report.content.read())
        self.assertEqual(pdf_export[2], "application/pdf")

    def test_regression_nested_components_columns(self):
        """
        Assert that columns in the form definition don't lead to template engine crashes.
        """
        submission = SubmissionFactory.from_components(
            completed=True,
            components_list=[
                {
                    "data": {
                        "values": [
                            {"label": "Hallo", "value": "hallo"},
                            {"label": "is it me", "value": "isItMe"},
                            {
                                "label": "you're looking for?",
                                "value": "youreLookingFor",
                            },
                        ]
                    },
                    "dataSrc": "values",
                    "key": "dropdownMetZoekfunctie",
                    "label": "Dropdown met zoekfunctie",
                    "showInEmail": True,
                },
                {
                    "key": "wachtwoord",
                    "label": "Wachtwoord",
                    "showInEmail": True,
                    "type": "password",
                },
                {
                    "key": "favorieteComponenten",
                    "label": "Favoriete componenten?",
                    "multiple": True,
                    "showInEmail": True,
                    "type": "textfield",
                },
                {
                    "key": "tijdstip",
                    "label": "Tijdstip",
                    "showInEmail": False,
                    "type": "time",
                },
                {
                    "components": [
                        {
                            "columns": [
                                {
                                    "components": [
                                        {
                                            "key": "dev1Naam",
                                            "label": "Naam",
                                            "showInEmail": False,
                                            "type": "textfield",
                                        }
                                    ],
                                },
                                {
                                    "components": [
                                        {
                                            "key": "dev1taken",
                                            "showInEmail": False,
                                            "type": "selectboxes",
                                            "values": [
                                                {
                                                    "label": "Backend",
                                                    "value": "backend",
                                                },
                                                {
                                                    "label": "Frontend",
                                                    "value": "frontend",
                                                },
                                                {
                                                    "label": "DevOops",
                                                    "value": "devOops",
                                                },
                                            ],
                                        }
                                    ],
                                },
                            ],
                            "key": "kolommen",
                            "label": "Kolommen",
                            "type": "columns",
                        },
                        {
                            "key": "nogEenOntwikkelaarToevoegen",
                            "label": "Nog een ontwikkelaar toevoegen?",
                            "showInEmail": False,
                            "type": "radio",
                            "values": [
                                {"label": "Ja", "value": "ja"},
                                {"label": "Nee", "value": "nee"},
                            ],
                        },
                    ],
                    "key": "dev1",
                    "label": "Ontwikkelaargegevens",
                    "legend": "Ontwikkelaargegevens",
                    "type": "fieldset",
                },
                {
                    "components": [
                        {
                            "columns": [
                                {
                                    "components": [
                                        {
                                            "key": "dev2Naam",
                                            "label": "Naam",
                                            "showInEmail": False,
                                            "type": "textfield",
                                        }
                                    ],
                                },
                                {
                                    "components": [
                                        {
                                            "key": "dev2taken",
                                            "label": "Taken",
                                            "showInEmail": False,
                                            "type": "selectboxes",
                                            "values": [
                                                {
                                                    "label": "Backend",
                                                    "value": "backend",
                                                },
                                                {
                                                    "label": "Frontend",
                                                    "value": "frontend",
                                                },
                                                {
                                                    "label": "DevOops",
                                                    "value": "devOops",
                                                },
                                            ],
                                        }
                                    ],
                                },
                            ],
                            "key": "kolommen1",
                            "label": "Kolommen",
                            "type": "columns",
                        }
                    ],
                    "key": "dev2",
                    "label": "Ontwikkelaargegevens",
                    "legend": "Ontwikkelaargegevens",
                },
            ],
            submitted_data={
                "dev1Naam": "Bart",
                "dev2Naam": "Silvia",
                "tijdstip": "11:00:00",
                "dev1taken": {"backend": True, "devOops": False, "frontend": False},
                "dev2taken": {"backend": True, "devOops": False, "frontend": True},
                "wachtwoord": "sdafsdfa",
                "favorieteComponenten": ["kaart"],
                "dropdownMetZoekfunctie": "isItMe",
                "nogEenOntwikkelaarToevoegen": "ja",
                "eMailadres": "foo@bar.nl",
            },
        )
        email_form_options = dict(
            to_emails=["foo@bar.nl", "bar@foo.nl"],
        )

        email_submission = EmailRegistration("email")
        email_submission.register_submission(submission, email_form_options)

        message = mail.outbox[0]

        message_html = message.alternatives[0][0]
        self.assertIn("Backend, Frontend", message_html)
