from .base import *

DEBUG = False

ALLOWED_HOSTS = [""]

INSTALLED_APPS += [
    'storages',
]

# S3 Storage
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": SECRET["S3"]["ACCESS"],
            "secret_key": SECRET["S3"]["SECRET"],
            "bucket_name": SECRET["S3"]["NAME"],
            "region_name": SECRET["S3"]["REGION"],
            "location": "media",
            "default_acl": "public-read",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": SECRET["S3"]["ACCESS"],
            "secret_key": SECRET["S3"]["SECRET"],
            "bucket_name": SECRET["S3"]["NAME"],
            "region_name": SECRET["S3"]["REGION"],
            "custom_domain": f'{SECRET["S3"]["NAME"]}.s3.amazonaws.com',
            "location": "static",
            "default_acl": "public-read",
        },
    },
}

# Static, Media URL
STATIC_URL = f'https://{SECRET["S3"]["NAME"]}.s3.amazonaws.com/static/'
MEDIA_URL = f'https://{SECRET["S3"]["NAME"]}.s3.amazonaws.com/media/'
