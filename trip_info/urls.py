from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TripInfoView

trip_info_list = TripInfoView.as_view({
    'post': 'create',
    'get': 'list',
})

trip_info = TripInfoView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = format_suffix_patterns([
    path('', trip_info_list, name='trip_info_list'),
    path('<int:pk>/', trip_info, name='trip_info'),
])
