from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema

from ..serializers import UserCreateSerializer

user_create_examples = [
    OpenApiExample(
        "Success Response",
        value={
            "status": "success",
            "data": {
                "email": "user@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "username": "johndoe",
            },
        },
        status_codes=["201"],
    ),
    OpenApiExample(
        "Validation Error",
        value={
            "status": "fail",
            "data": {"email": ["user with this email already exists."]},
        },
        status_codes=["400"],
    ),
]

user_create_schema = extend_schema(
    summary="Create new user",
    description="Creates a new user account with the provided information.",
    request=UserCreateSerializer,
    responses={
        201: OpenApiResponse(
            response=UserCreateSerializer,
            description="User created successfully",
            examples=user_create_examples[:1],
        ),
        400: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Validation error",
            examples=user_create_examples[1:],
        ),
    },
    tags=["Users"],
)
