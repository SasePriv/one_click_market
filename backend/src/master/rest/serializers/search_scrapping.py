from rest_framework import serializers

from master.models import SearchScraping


class SearchScrappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchScraping
        fields = ('guid', 'search_json', 'text', 'customer')
