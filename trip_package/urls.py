from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TripPackageView

router = DefaultRouter()
router.register('', TripPackageView)

urlpatterns = [
    path('', include(router.urls))
]