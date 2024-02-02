import logging

from django.contrib import admin

from ..models import Product

logger = logging.getLogger(__name__)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'unit_price']
    search_fields = ['name', 'id']
