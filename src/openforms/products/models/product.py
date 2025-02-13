import uuid as _uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tinymce.models import HTMLField


class Product(models.Model):
    """
    Product model for a PDC (Producten en Diensten Catalogus) definition.
    """

    uuid = models.UUIDField(
        _("UUID"),
        default=_uuid.uuid4,
        help_text=_("Globally unique identifier"),
        unique=True,
    )
    name = models.CharField(_("name"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)

    information = HTMLField(
        _("information"),
        blank=True,
        help_text=_(
            "Information text to be displayed in the confirmation page and confirmation email."
        ),
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
