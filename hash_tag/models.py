from django.db import models
from django.utils.translation import ugettext_lazy as _


class HashTag(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name=_('태그 이름'),
    )

    def __str__(self):
        return self.name
