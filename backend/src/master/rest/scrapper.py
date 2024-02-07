import logging

from requests import Response, Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from master.helper.web_scrapping_helper import WebScrappingHelper
from master.rest.serializers import ScrapperSerializer

logger = logging.getLogger(__name__)


class ScrapperView(APIView):
    def post(self, request: Request):
        text = request.data.get('text')
        scrap = WebScrappingHelper.get_name_and_prices(keyword=text)
        serializer = ScrapperSerializer(scrap)
        return Response(serializer.data, status=status.HTTP_200_OK)
