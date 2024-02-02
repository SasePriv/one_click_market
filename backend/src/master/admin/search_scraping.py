import logging

from django.contrib import admin

from ..models import SearchScraping

logger = logging.getLogger(__name__)


@admin.register(SearchScraping)
class SearchScraping(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['name', 'id']
