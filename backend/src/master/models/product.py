import logging
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class Product(models.Model):
    class Meta:
        verbose_name_plural = _("Productos")
        verbose_name = _("Producto")

    id = models.AutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=32, unique=True, null=False, blank=False, help_text=_("Nombre del producto"),
                            verbose_name=_("Nombre del producto"))
    price = models.FloatField(null=False, blank=False, default=0.0, verbose_name=_("Precio del producto"))
    unit_price = models.FloatField(null=False, blank=False, default=0.0, verbose_name=_("Precio del producto"))


