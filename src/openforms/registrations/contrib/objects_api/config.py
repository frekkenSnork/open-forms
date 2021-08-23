from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from openforms.utils.validators import validate_rsin


class ObjectsAPIOptionsSerializer(serializers.Serializer):
    objecttype = serializers.URLField(
        label=_("Objecttype"),
        help_text=_(
            "URL that points to the ProductAanvraag objecttype in the Objecttypes API. "
            "The objecttype should have the following three attributes: "
            "1) submission_id; "
            "2) type (the type of productaanvraag); "
            "3) data (the submitted form data)"
        ),
        required=False,
    )
    objecttype_version = serializers.IntegerField(
        label=_("Objecttype version"),
        help_text=_("Version of the objecttype in the Objecttypes API"),
        required=False,
    )
    productaanvraag_type = serializers.CharField(
        label=_("Productaanvraag type"),
        help_text=_("The type of ProductAanvraag"),
        required=False,
    )
    informatieobjecttype_submission_report = serializers.URLField(
        label=_("Submission report informatieobjecttype"),
        help_text=_(
            "URL that points to the Informatieobjecttype in the Documenten API "
            "to be used for the submission report"
        ),
        required=False,
    )
    informatieobjecttype_attachment = serializers.URLField(
        label=_("Attachment informatieobjecttype"),
        help_text=_(
            "URL that points to the Informatieobjecttype in the Documenten API "
            "to be used for the submission attachments"
        ),
        required=False,
    )
    organisatie_rsin = serializers.CharField(
        label=_("Organisation RSIN"),
        required=False,
        validators=[validate_rsin],
        help_text=_("RSIN of organization, which creates the INFORMATIEOBJECT"),
    )
