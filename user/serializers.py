"""
Serializer for the User API.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User Object."""

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        """create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
        