from decouple import config

from .base import *

ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3"}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
