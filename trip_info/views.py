from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import TripInfo
from .serializers import TripInfoSerializer, TripInfoDetailSerializer


class TripInfoView(viewsets.ReadOnlyModelViewSet):
    """
    여행 정보

    ---
    여행 정보 관련 API
    """
    queryset = TripInfo.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'details':
            return TripInfoDetailSerializer
        return TripInfoSerializer

    @action(detail=True)
    def details(self, request, pk):
        info = self.get_object()
        qs = info.detail.all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def like(self, request, pk):
        info = self.get_object()
        info.like_user_set.add(self.request.user)
        info.save()
        serializer = self.get_serializer(info)
        return Response(serializer.data)
