from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CityView

router = DefaultRouter()
router.register('', CityView)

urlpatterns = [
    path('', include(router.urls)),
]
