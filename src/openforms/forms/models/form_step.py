import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from ordered_model.models import OrderedModel

from openforms.utils.fields import StringUUIDField

from ..constants import AvailabilityOptions
from .utils import literal_getter


class FormStep(OrderedModel):
    """
    Through table for Form -> FormDefinitions.
    Allows for FormDefinitions to be reused as FormSteps in other Form instances.
    """

    uuid = StringUUIDField(_("UUID"), unique=True, default=uuid.uuid4)
    form = models.ForeignKey("forms.Form", on_delete=models.CASCADE)
    form_definition = models.ForeignKey(
        "forms.FormDefinition", on_delete=models.PROTECT
    )

    # step properties/flow control
    optional = models.BooleanField(
        _("optional"),
        default=False,
        help_text=_(
            "Designates whether this step is an optional step in the form. "
            "Currently used for form-rendering purposes, this is not (yet) used for "
            "validation purposes."
        ),
    )
    availability_strategy = models.CharField(
        _("availability"),
        max_length=50,
        choices=AvailabilityOptions,
        default=AvailabilityOptions.always,
        help_text=_(
            "Availability strategy to use. A step must be available before it can be "
            "filled out. Note that this is not validated (yet) during step submission."
        ),
    )

    previous_text = models.CharField(
        _("step previous text"),
        max_length=50,
        blank=True,
        help_text=_(
            "The text that will be displayed in the form step to go to the previous step. "
            "Leave blank to get value from global configuration."
        ),
    )
    save_text = models.CharField(
        _("step save text"),
        max_length=50,
        blank=True,
        help_text=_(
            "The text that will be displayed in the form step to save the current information. "
            "Leave blank to get value from global configuration."
        ),
    )
    next_text = models.CharField(
        _("step next text"),
        max_length=50,
        blank=True,
        help_text=_(
            "The text that will be displayed in the form step to go to the next step. "
            "Leave blank to get value from global configuration."
        ),
    )

    order_with_respect_to = "form"

    get_previous_text = literal_getter("previous_text", "form_step_previous_text")
    get_save_text = literal_getter("save_text", "form_step_save_text")
    get_next_text = literal_getter("next_text", "form_step_next_text")

    class Meta:
        verbose_name = _("form step")
        verbose_name_plural = _("form steps")

    def __str__(self):
        return _("Form step {order}").format(order=self.order)

    def iter_components(self, recursive=True):
        yield from self.form_definition.iter_components(recursive=recursive)
