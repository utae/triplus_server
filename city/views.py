from rest_framework import viewsets

from .models import City
from .serializers import CitySerializer


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
