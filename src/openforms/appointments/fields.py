from django.db.models.fields import CharField

from .constants import UNIQUE_ID_MAX_LENGTH
from .registry import register
from .validators import PluginValidator


class AppointmentBackendChoiceField(CharField):
    def __init__(self, *args, **kwargs):
        self.registry = kwargs.pop("registry", register)

        kwargs.setdefault("max_length", UNIQUE_ID_MAX_LENGTH)
        if kwargs["max_length"] > UNIQUE_ID_MAX_LENGTH:
            raise ValueError("'max_length' is capped at {UNIQUE_ID_MAX_LENGTH}")

        super().__init__(*args, **kwargs)

        self.validators.append(PluginValidator(self.registry))

    def formfield(self, **kwargs):
        """
        Force this into a choices field.
        """
        monkeypatch = not self.choices
        if monkeypatch:
            _old = self.choices
            self.choices = self._get_plugin_choices()
        field = super().formfield(**kwargs)
        if monkeypatch:
            self.choices = _old
        return field

    def _get_plugin_choices(self):
        return [(plugin.unique_identifier, plugin.name) for plugin in self.registry]
