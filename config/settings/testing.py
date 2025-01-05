from .base import *
from .base import config

ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3"}

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
