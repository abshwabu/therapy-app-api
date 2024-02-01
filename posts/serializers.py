"""
serializers for post APIs.
"""
from rest_framework import serializers

from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts"""

    class Meta:
        model = Post
        fields = ['id', 'title',]
        read_only_fields = ['id']


class PostDetailSerializer(PostSerializer):
    """serializer for post details."""

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['content']
