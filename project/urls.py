from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import SingerViewSet, SongViewSet

router = DefaultRouter()
router.register('singer', SingerViewSet, basename='singer')
router.register('song', SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
