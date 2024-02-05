"""
serializers for post APIs.
"""
from rest_framework import serializers

from core.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    """serializer for objects."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts"""

    tags = TagSerializer(many=True, required=False)


    class Meta:
        model = Post
        fields = ['id', 'title','tags']
        read_only_fields = ['id']


class PostDetailSerializer(PostSerializer):
    """serializer for post details."""

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['content']



