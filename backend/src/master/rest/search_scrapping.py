import logging

from rest_framework import viewsets

from master.models import SearchScraping
from master.rest.serializers import SearchScrappingSerializer

logger = logging.getLogger(__name__)


class SearchScrappingViewSet(viewsets.ModelViewSet):
    serializer_class = SearchScrappingSerializer
    queryset = SearchScraping.objects.all()
    lookup_field = 'guid'
