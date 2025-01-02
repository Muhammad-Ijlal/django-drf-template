from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.extensions import OpenApiAuthenticationExtension


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Override the default get_user method to include a check for 'deleted_at'.
        """
        user = super().get_user(validated_token)
        if user.deleted_at is not None:
            return None
        return user


class CustomJWTAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = CustomJWTAuthentication
    name = "CustomJWTAuthentication"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Custom JWT authentication with additional validation",
        }
