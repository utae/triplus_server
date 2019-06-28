from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CityView

city_list = CityView.as_view({
    'get': 'list',
})

urlpatterns = format_suffix_patterns([
    path('', city_list, name='trip_info_list'),
])
