from datetime import timedelta

from decouple import config

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    "rest_framework_simplejwt.authentication.JWTAuthentication",
)

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=60),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": config("SIGNING_KEY"),
    "VERIFYING_KEY": "",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
}

# Link to the custom user model
AUTH_USER_MODEL = "core.User"

# Google provider configuration
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_CLIENT_ID": config("GOOGLE_CLIENT_ID"),
        "OAUTH_CLIENT_SECRET": config("GOOGLE_CLIENT_SECRET"),
        "FETCH_USERINFO": True,
    },
}

SOCIALACCOUNT_ADAPTER = "apps.agents.utils.CustomSocialAccountAdapter"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "optional"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
