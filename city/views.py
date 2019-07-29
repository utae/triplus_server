from rest_framework import viewsets

from .models import City
from .serializers import CitySerializer


class CityView(viewsets.ReadOnlyModelViewSet):
    """
    도시

    ---
    도시 관련 API
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
