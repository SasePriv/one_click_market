from rest_framework import routers
from django.urls import path
from .rest import SearchScrappingViewSet, ScrapperView

app_name = 'master'

router = routers.DefaultRouter()

router.register('master/search_scrapping', SearchScrappingViewSet, basename='SearchScrapping')

urlpatterns = [
    path('master/scrapper', ScrapperView.as_view()),
]
