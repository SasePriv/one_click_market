import logging
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class Customer(models.Model):
    class Meta:
        verbose_name_plural = _("Customers")
        verbose_name = _("Customers")

    id = models.AutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=32, unique=True, null=False, blank=False, help_text=_("Nombre del Customer"),
                            verbose_name=_("Nombre del Customer"))
