from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView


from master.urls import router as master_router

if hasattr(settings, 'ADMIN_SITE_HEADER'):
    admin.site.site_header = settings.ADMIN_SITE_HEADER
    admin.site.site_title = settings.ADMIN_SITE_HEADER

router = routers.DefaultRouter()

router.registry.extend(master_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True))]
