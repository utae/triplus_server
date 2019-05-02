from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('이메일'),
        max_length=191,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_('이름'),
        max_length=30,
    )
    is_active = models.BooleanField(
        verbose_name=_('활성'),
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name=_('관리자'),
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('가입시간'),
        auto_now_add=True,
    )
    profile_img = models.ImageField(
        verbose_name=_('프로필 사진'),
        null=True,
        blank=True,
        upload_to='image/profile_img',
    )
    # # 이 필드는 레거시 시스템 호환을 위해 추가할 수도 있다.
    # salt = models.CharField(
    #     verbose_name=_('Salt'),
    #     max_length=10,
    #     blank=True
    # )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Dose the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Dose the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_admin

    get_full_name.short_description = _('Full name')