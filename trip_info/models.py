from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from hash_tag.models import HashTag


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
        verbose_name=_('작성시간'),
        auto_now_add=True,
    )

    last_modified_at = models.DateTimeField(
        verbose_name=_('최근 수정시간'),
        auto_now=True,
    )

    page_cnt = models.PositiveSmallIntegerField(
        verbose_name=_('페이지 수'),
    )

    main_img = models.ImageField(
        verbose_name=_('메인 이미지'),
    )

    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_trip_info_set',
        verbose_name=_('좋아요 유저'),
    )

    comment_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='comment_trip_info_set',
        through="TripInfoComment",
        verbose_name=_('댓글 유저'),
    )

    hash_tag_set = models.ManyToManyField(
        HashTag,
        related_name='trip_info_set',
        verbose_name=_('해시 태그'),
    )


class TripInfoDetail(models.Model):

    trip_info = models.ForeignKey(
        TripInfo,
        on_delete=models.CASCADE,
        verbose_name=_('원게시물')
    )

    text = models.TextField(
        verbose_name=_('내용'),
    )

    image = models.ImageField(
        verbose_name=_('이미지'),
    )


class TripInfoComment(models.Model):

    trip_info = models.ForeignKey(
        TripInfo,
        on_delete=models.CASCADE,
        verbose_name=_('원게시물'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('작성자')
    )

    text = models.TextField(
        verbose_name=_('댓글 내용'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('작성시간'),
    )

    last_modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('최근 수정시간'),
    )
