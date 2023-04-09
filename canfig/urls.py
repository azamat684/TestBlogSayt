from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api.views import ProjectViewSet
router = DefaultRouter()
router.register(r'projects',ProjectViewSet,basename='projects'),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('api/v1/',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )