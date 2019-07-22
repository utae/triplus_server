from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'triplus',
        'USER': 'root',
        'PASSWORD': 'globetrip12+',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}

ACCOUNT_EMAIL_MAX_LENGTH = 191

AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'triplus'
AWS_ACCESS_KEY_ID = 'AKIA3WGEA6MQHA44QH65'
AWS_SECRET_ACCESS_KEY = '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'

AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static Setting
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Media Setting
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Root Setting
# STATIC_ROOT = '%s/static' % STORAGE_PATH
# MEDIA_ROOT = '%s/media' % STORAGE_PATH
