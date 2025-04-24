from decouple import config

from .base import *

DEBUG = True

ALLOWED_HOSTS = []
CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "emails")
