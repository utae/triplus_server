from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import TripPackage
from .serializers import TripPackageSerializer


class TripPackageView(viewsets.ReadOnlyModelViewSet):
    """
    여행 상품

    ---
    여행 상품 관련 API
    """
    queryset = TripPackage.objects.all()
    serializer_class = TripPackageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @detail_route()
    def like(self, request, pk):
        package = self.get_object()
        package.like_user_set.add(self.request.user)
        package.save()
        serializer = self.get_serializer(package)
        return Response(serializer.data)
