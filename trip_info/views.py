from rest_framework import viewsets, permissions

from .models import TripInfo
from .serializers import TripInfoSerializer


class TripInfoView(viewsets.ModelViewSet):
    """
    여행 정보 생성 및 리스트 조회

    ---
    title : 제목
    city : 도시
    main_img : 메인 이미지
    hash_tag_set : 해시태그
    """
    queryset = TripInfo.objects.all()
    serializer_class = TripInfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
