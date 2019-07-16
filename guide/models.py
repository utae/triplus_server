from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Guide(models.Model):

    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('계정'),
    )

    phone = models.CharField(
        verbose_name=_('핸드폰번호'),
        max_length=11,
    )


