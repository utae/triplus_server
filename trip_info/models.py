from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class TripInfo(models.Model):

    title = models.CharField(
        verbose_name=_('제목'),
        max_length=100,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('작성자'),
    )

    created_at = models.DateTimeField(
        verbose_name=_('작성일'),
        auto_now_add=True,
    )

    last_modified_at = models.DateTimeField(
        verbose_name=_('최근 수정일'),
        auto_now=True,
    )

    page_cnt = models.IntegerField(
        verbose_name=_('페이지 수'),
    )

    main_img = models.ImageField(
        verbose_name=_('메인 이미지'),
    )
