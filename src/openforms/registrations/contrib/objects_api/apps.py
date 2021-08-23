from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ObjectsAPIPluginConfig(AppConfig):
    name = "openforms.registrations.contrib.objects_api"
    label = "registrations_objects_api"
    verbose_name = _("Objects API plugin")

    def ready(self):
        # register plugin
        from . import plugin  # noqa
