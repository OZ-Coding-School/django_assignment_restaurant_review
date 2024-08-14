from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [""]

INSTALLED_APPS += [
    'storages',
]

# Static
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / '.static_root'

# Media
MEDIA_ROOT = BASE_DIR / 'media'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECRET['DB']['NAME'],               # 데이터베이스 이름
        'USER': SECRET['DB']['USER'],               # 사용자 이름
        'PASSWORD': SECRET['DB']['PASSWORD'],       # 비밀번호
        'HOST': SECRET['DB']['HOST'],               # 데이터베이스 서버 주소
        'PORT': SECRET['DB']['PORT'],               # MySQL의 기본 포트
    }
}

AWS_ACCESS_KEY_ID = SECRET['S3']['ACCESS']
AWS_SECRET_ACCESS_KEY = SECRET['S3']['SECRET']
AWS_STORAGE_BUCKET_NAME = SECRET['S3']['NAME']
AWS_S3_REGION_NAME = SECRET['S3']['REGION']

AWS_LOCATION = "static"
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# S3 static
STATICFILES_STORAGE = 'storages.backends.s3.S3Storage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# S3 media
DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

