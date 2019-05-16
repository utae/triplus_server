from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from hash_tag.models import HashTag


def trip_info_img_path(instance, filename):
    return 'image/trip_info/{id}/{filename}'.format(id=instance.id, filename=filename)


def trip_info_detail_img_path(instance, filename):
    return 'image/trip_info/{trip_info_id}/{filename}'.format(trip_info_id=instance.trip_info.id, filename=filename)


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

    main_img = models.ImageField(
        verbose_name=_('메인 이미지'),
        upload_to=trip_info_img_path,
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

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.id is None and self.main_img is not None:
            temp_image = self.main_img
            self.main_img = None
            super().save(*args, **kwargs)
            self.main_img = temp_image
        super().save(*args, **kwargs)


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
        upload_to=trip_info_detail_img_path,
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
