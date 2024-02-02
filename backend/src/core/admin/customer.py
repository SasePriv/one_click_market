import logging

from django.contrib import admin

from ..models import Customer

logger = logging.getLogger(__name__)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']
