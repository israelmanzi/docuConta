from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'role', 'created_at', 'refresh_token')
        extra_kwargs = {'password': {'write_only': True}}
