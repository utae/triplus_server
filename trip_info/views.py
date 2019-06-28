from rest_framework import viewsets, permissions

from .models import TripInfo
from .serializers import TripInfoSerializer


class TripInfoView(viewsets.ModelViewSet):
    queryset = TripInfo.objects.all()
    serializer_class = TripInfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
