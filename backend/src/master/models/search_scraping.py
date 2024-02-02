import logging
import uuid

from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _

from core.models import Customer

logger = logging.getLogger(__name__)


class SearchScraping(models.Model):
    class Meta:
        verbose_name_plural = _("Searchs Scraping")
        verbose_name = _("Search Scraping")

    id = models.AutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    search_json = JSONField(null=False, blank=True, default=dict,
                            verbose_name=_("JSON de del scrapper de la busqueda"))
    text = models.TextField(max_length=256, null=False, blank=True, default='',
                            help_text=_('Texto de busqueda'),
                            verbose_name=_('Texto de busqueda'))
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE, related_name="search_scraping",
                                 verbose_name=_("Cliente"))
