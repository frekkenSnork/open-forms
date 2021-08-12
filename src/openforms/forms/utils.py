import json
import zipfile
from uuid import uuid4

from django.conf import settings
from django.db import transaction

from rest_framework.exceptions import ValidationError
from rest_framework.test import APIRequestFactory

from .api import serializers as api_serializers
from .api.serializers import (
    FormDefinitionSerializer,
    FormExportSerializer,
    FormLogicSerializer,
    FormStepSerializer,
)
from .models import Form, FormDefinition, FormLogic, FormStep

IMPORT_ORDER = {
    "formDefinitions": FormDefinition,
    "forms": Form,
    "formSteps": FormStep,
    "formLogic": FormLogic,
}


def _get_mock_request():
    factory = APIRequestFactory()
    first_allowed_host = (
        settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "testserver"
    )
    server_name = first_allowed_host if first_allowed_host != "*" else "testserver"
    request = factory.get("/", SERVER_NAME=server_name)
    return request


def form_to_json(form_id: int) -> dict:
    form = Form.objects.get(pk=form_id)

    # Ignore products in the export
    form.product = None

    form_steps = FormStep.objects.filter(form__pk=form_id).select_related(
        "form_definition"
    )

    form_definitions = FormDefinition.objects.filter(
        pk__in=form_steps.values_list("form_definition", flat=True)
    )

    form_logic = FormLogic.objects.filter(form_step__form=form)

    request = _get_mock_request()

    forms = [FormExportSerializer(instance=form, context={"request": request}).data]
    form_definitions = FormDefinitionSerializer(
        instance=form_definitions,
        many=True,
        context={"request": request, "handle_custom_types": False},
    ).data
    form_steps = FormStepSerializer(
        instance=form_steps, many=True, context={"request": request}
    ).data
    form_logic = FormLogicSerializer(
        instance=form_logic, many=True, context={"request": request}
    ).data

    resources = {
        "forms": json.dumps(forms),
        "formSteps": json.dumps(form_steps),
        "formDefinitions": json.dumps(form_definitions),
        "formLogic": json.dumps(form_logic),
    }

    return resources


def export_form(form_id, archive_name=None, response=None):
    resources = form_to_json(form_id)

    outfile = response or archive_name
    with zipfile.ZipFile(outfile, "w") as zip_file:
        for name, data in resources.items():
            zip_file.writestr(f"{name}.json", data)


@transaction.atomic
def import_form(import_file):
    uuid_mapping = {}

    request = _get_mock_request()
    created_form_definitions = []

    created_form = None
    with zipfile.ZipFile(import_file, "r") as zip_file:
        for resource, model in IMPORT_ORDER.items():
            if f"{resource}.json" in zip_file.namelist():
                data = zip_file.read(f"{resource}.json").decode()

                for old, new in uuid_mapping.items():
                    data = data.replace(old, new)

                if resource == "formDefinitions":
                    serializer = api_serializers.FormDefinitionSerializer
                if resource == "forms":
                    serializer = api_serializers.FormSerializer
                if resource == "formSteps":
                    serializer = api_serializers.FormStepSerializer
                if resource == "formLogic":
                    serializer = api_serializers.FormLogicSerializer

                for entry in json.loads(data):
                    if "uuid" in entry:
                        old_uuid = entry["uuid"]
                        entry["uuid"] = str(uuid4())

                    if resource == "forms":
                        entry["active"] = False

                    deserialized = serializer(
                        data=entry,
                        context={"request": request, "form": created_form},
                    )

                    try:
                        deserialized.is_valid(raise_exception=True)
                        deserialized.save()
                        if resource == "forms":
                            created_form = deserialized.instance

                        # The FormSerializer/FormStepSerializer/FormLogicSerializer have the uuid as a read only field.
                        # So the mapping between the old uuid and the new needs to be done after the instance is saved.
                        if hasattr(deserialized.instance, "uuid") and "uuid" in entry:
                            uuid_mapping[old_uuid] = str(deserialized.instance.uuid)
                    except ValidationError as e:
                        if (
                            resource == "formDefinitions"
                            and "slug" in e.detail
                            and e.detail["slug"][0].code == "unique"
                        ):
                            existing_fd = FormDefinition.objects.get(slug=entry["slug"])
                            existing_fd_hash = existing_fd.get_hash()
                            imported_fd_hash = FormDefinition(
                                configuration=entry["configuration"]
                            ).get_hash()

                            if existing_fd_hash == imported_fd_hash:
                                # The form definition that is being imported
                                # is identical to the existing form definition
                                # with the same slug, use existing instead
                                # of creating new definition
                                uuid_mapping[old_uuid] = existing_fd.uuid
                            else:
                                # The imported form definition configuration
                                # is different, create a new form definition
                                entry.pop("url")
                                entry.pop("uuid")
                                new_fd = FormDefinition(**entry)
                                new_fd.save()
                                uuid_mapping[old_uuid] = str(new_fd.uuid)

                                created_form_definitions.append(new_fd.slug)
                        else:
                            raise e
    return created_form_definitions


def remove_key_from_dict(dictionary, key):
    for dict_key in list(dictionary.keys()):
        if key == dict_key:
            del dictionary[key]
        elif isinstance(dictionary[dict_key], dict):
            remove_key_from_dict(dictionary[dict_key], key)
        elif isinstance(dictionary[dict_key], list):
            for value in dictionary[dict_key]:
                if isinstance(value, dict):
                    remove_key_from_dict(value, key)
