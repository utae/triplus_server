from django.db import models
from django.utils.translation import ugettext_lazy as _

from hash_tag.models import HashTag


def city_img_path(instance, filename):
    return 'image/city/{name}/{filename}'.format(name=instance.name, filename=filename)


class City(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name=_('도시 이름'),
    )

    main_img = models.ImageField(
        verbose_name=_('메인 이미지'),
        upload_to=city_img_path,
    )

    hash_tag_set = models.ManyToManyField(
        HashTag,
        related_name='city_hash_tag_set',
        verbose_name=_('해시 태그'),
    )

    def __str__(self):
        return self.name
