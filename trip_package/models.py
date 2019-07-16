from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from city.models import City
from guide.models import Guide
from hash_tag.models import HashTag


def trip_package_main_img_path(instance, filename):
    return 'image/trip_package/{trip_package_id}/main/{filename}'.format(
        trip_package_id=instance.trip_package.id,
        filename=filename)


def trip_package_detail_img_path(instance, filename):
    return 'image/trip_package/{trip_package_id}/detail/{filename}'.format(
        trip_package_id=instance.trip_package.id,
        filename=filename)


def trip_package_review_img_path(instance, filename):
    return 'image/trip_package/{trip_package_id}/review/{filename}'.format(
        trip_package_id=instance.trip_package.id,
        filename=filename)


class TripPackage(models.Model):

    title = models.CharField(
        verbose_name=_('제목'),
        max_length=100,
    )

    sub_title = models.CharField(
        verbose_name=_('부제'),
        max_length=100,
    )

    created_at = models.DateTimeField(
        verbose_name=_('작성시간'),
        auto_now_add=True,
    )

    last_modified_at = models.DateTimeField(
        verbose_name=_('최근 수정시간'),
        auto_now=True,
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_('도시'),
    )

    address = models.CharField(
        verbose_name=_('메인주소'),
        max_length=191,
    )

    price = models.PositiveIntegerField(
        verbose_name=_('가격'),
    )

    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        verbose_name=_('가이드'),
    )

    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_trip_package_set',
        verbose_name=_('좋아요 유저'),
        blank=True,
    )

    hash_tag_set = models.ManyToManyField(
        HashTag,
        related_name='trip_package_hash_tag_set',
        verbose_name=_('해시 태그'),
    )

    review_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='trip_package_review_set',
        through="TripPackageReview",
        verbose_name=_('리뷰 유저'),
        blank=True,
    )


class TripPackageMainImg(models.Model):

    trip_package = models.ForeignKey(
        TripPackage,
        on_delete=models.CASCADE,
        verbose_name=_('상품')
    )

    image = models.ImageField(
        verbose_name=_('이미지'),
        upload_to=trip_package_main_img_path,
    )


class TripPackageDetail(models.Model):

    trip_package = models.ForeignKey(
        TripPackage,
        on_delete=models.CASCADE,
        verbose_name=_('상품')
    )

    image = models.ImageField(
        verbose_name=_('이미지'),
        upload_to=trip_package_detail_img_path,
        default='',
        blank=True
    )

    text = models.TextField(
        verbose_name=_('내용'),
        default='',
        blank=True
    )


class TripPackageReview(models.Model):

    trip_package = models.ForeignKey(
        TripPackage,
        on_delete=models.CASCADE,
        verbose_name=_('상품')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('작성자')
    )

    rating = models.CharField(
        verbose_name=_('평점'),
        max_length=1,
        validators=[RegexValidator(r'^[1,5]$')],
    )

    image = models.ImageField(
        verbose_name=_('이미지'),
        upload_to=trip_package_review_img_path,
        default='',
        blank=True,
    )

    text = models.TextField(
        verbose_name=_('리뷰 내용'),
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('작성시간'),
    )

    last_modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('최근 수정시간'),
    )


class TripPackageAddition(models.Model):

    trip_package = models.ForeignKey(
        TripPackage,
        on_delete=models.CASCADE,
        verbose_name=_('상품')
    )

    title = models.CharField(
        verbose_name=_('제목'),
        max_length=50,
    )

    text = models.TextField(
        verbose_name=_('내용'),
        default='',
        blank=True
    )
