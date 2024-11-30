from apps.core.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
