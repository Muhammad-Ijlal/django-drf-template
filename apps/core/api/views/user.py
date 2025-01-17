import logging

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from config.utils.response import JSendResponse, JSendResponseMixin

from ...models import User
from ..schema.user import user_create_schema
from ..serializers import UserCreateSerializer

logger = logging.getLogger(__name__)


@user_create_schema
class UserCreateView(CreateAPIView, JSendResponseMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Create a new user."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)

        return JSendResponse.success(
            data=serializer.data, status_code=status.HTTP_201_CREATED, headers=headers
        )
