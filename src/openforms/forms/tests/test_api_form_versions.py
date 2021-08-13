import datetime

from django.http import HttpRequest
from django.urls import reverse

from freezegun import freeze_time
from rest_framework import status
from rest_framework.test import APITestCase

from openforms.accounts.tests.factories import UserFactory

from ...submissions.tests.form_logic.factories import FormLogicFactory
from ..models import FormDefinition, FormLogic, FormStep, FormVersion
from .factories import (
    FormDefinitionFactory,
    FormFactory,
    FormStepFactory,
    FormVersionFactory,
)

EXPORT_BLOB = {
    "forms": '[{"uuid": "324cadce-a627-4e3f-b117-37ca232f16b2", "name": "Test Form 1", "login_required": false, "authentication_backends": ["digid-mock", "digid"], "product": null, "slug": "auth-plugins", "url": "http://testserver/api/v1/forms/324cadce-a627-4e3f-b117-37ca232f16b2", "show_progress_indicator": true, "maintenance_mode": false, "active": true, "is_deleted": false}]',
    "formSteps": '[{"uuid": "3ca01601-cd20-4746-bce5-baab47636823", "index": 0, "slug": "test-step-1", "form_definition": "http://testserver/api/v1/form-definitions/f0dad93b-333b-49af-868b-a6bcb94fa1b8", "form": "http://testserver/api/v1/forms/324cadce-a627-4e3f-b117-37ca232f16b2"}]',
    "formDefinitions": '[{"url": "http://testserver/api/v1/form-definitions/f0dad93b-333b-49af-868b-a6bcb94fa1b8", "uuid": "f0dad93b-333b-49af-868b-a6bcb94fa1b8", "name": "Test Definition 1", "slug": "test-definition-1", "configuration": {"test": "1"}}]',
    "formLogic": '[{"uuid": "b92342be-05e0-4070-b2cc-1b88af472091", "form_step": "http://testserver/api/v1/forms/324cadce-a627-4e3f-b117-37ca232f16b2/steps/3ca01601-cd20-4746-bce5-baab47636823", "component": "test", "actions": [{"action": {"type": "disable-next"}}], "json_logic_trigger": {"==": [1, 1]}}]',
}


class FormVersionSaveAPITests(APITestCase):
    def test_auth_required(self):
        form = FormFactory.create()
        url = reverse("api:form-versions-list", args=(form.uuid,))

        response = self.client.post(url)

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_must_be_staff_user(self):
        user = UserFactory.create(username="test", password="test", is_staff=False)
        form = FormFactory.create()

        versions = FormVersion.objects.filter(form=form)

        self.assertEqual(0, versions.count())

        self.client.login(
            request=HttpRequest(), username=user.username, password="test"
        )
        url = reverse("api:form-versions-list", args=(form.uuid,))
        response = self.client.post(url)

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    @freeze_time("2020-12-11T10:53:19+01:00")
    def test_save_version(self):
        user = UserFactory.create(username="test", password="test", is_staff=True)
        form = FormFactory.create()

        versions = FormVersion.objects.filter(form=form)

        self.assertEqual(0, versions.count())

        self.client.login(
            request=HttpRequest(), username=user.username, password="test"
        )
        url = reverse("api:form-versions-list", args=(form.uuid,))
        response = self.client.post(url)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        versions = FormVersion.objects.filter(form=form)

        self.assertEqual(1, versions.count())

        version = versions.first()

        self.assertEqual(form, version.form)
        self.assertEqual(
            datetime.datetime.strptime(
                "2020-12-11T10:53:19+01:00", "%Y-%m-%dT%H:%M:%S%z"
            ),
            version.created,
        )

    def test_list_versions(self):
        user = UserFactory.create(username="test", password="test", is_staff=True)
        form_1 = FormFactory.create()
        form_2 = FormFactory.create()

        FormVersionFactory.create(form=form_1)
        FormVersionFactory.create(form=form_2)

        self.assertEqual(2, FormVersion.objects.all().count())

        self.client.login(
            request=HttpRequest(), username=user.username, password="test"
        )
        url = reverse("api:form-versions-list", args=(form_1.uuid,))
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))


class FormVersionRestoreAPITests(APITestCase):
    def test_auth_required(self):
        form = FormFactory.create()
        form_version = FormVersionFactory.create(form=form)
        url = reverse(
            "api:form-versions-restore",
            kwargs={"form_uuid_or_slug": form.uuid, "uuid": form_version.uuid},
        )

        response = self.client.post(url)

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_must_be_staff_user(self):
        user = UserFactory.create(username="test", password="test", is_staff=False)
        form = FormFactory.create()
        form_version = FormVersionFactory.create(form=form)

        self.client.login(
            request=HttpRequest(), username=user.username, password="test"
        )
        url = reverse(
            "api:form-versions-restore",
            kwargs={"form_uuid_or_slug": form.uuid, "uuid": form_version.uuid},
        )
        response = self.client.post(url)

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_restore_version(self):
        form_definition = FormDefinitionFactory.create(
            slug="test-definition-2", configuration={"test": "2"}
        )
        form = FormFactory.create(name="Test Form 2")
        form_step = FormStepFactory.create(form=form, form_definition=form_definition)
        FormLogicFactory.create(form_step=form_step)

        version = FormVersion.objects.create(
            form=form,
            created=datetime.datetime(2021, 7, 21, 12, 00, 00),
            export_blob=EXPORT_BLOB,
        )

        user = UserFactory.create(username="test", password="test", is_staff=True)
        self.client.login(
            request=HttpRequest(), username=user.username, password="test"
        )
        url = reverse(
            "api:form-versions-restore",
            kwargs={"form_uuid_or_slug": form.uuid, "uuid": version.uuid},
        )

        self.assertEqual(1, FormVersion.objects.all().count())
        self.assertEqual(1, FormDefinition.objects.all().count())

        response = self.client.post(url, data={"uuid": version.uuid})

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        form.refresh_from_db()

        self.assertEqual(1, FormVersion.objects.all().count())
        self.assertEqual("Test Form 1", form.name)
        self.assertEqual(2, FormDefinition.objects.all().count())

        form_steps = FormStep.objects.filter(form=form)
        form_logic = FormLogic.objects.filter(form_step__form=form)

        self.assertEqual(1, form_steps.count())
        self.assertEqual(1, form_logic.count())

        restored_form_definition = form_steps.get().form_definition

        self.assertEqual("Test Definition 1", restored_form_definition.name)
        self.assertEqual("test-definition-1", restored_form_definition.slug)
        self.assertEqual({"test": "1"}, restored_form_definition.configuration)
