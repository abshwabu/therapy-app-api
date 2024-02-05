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

    def create(self, validated_data):
        """Create a new post."""
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            post.tags.add(tag_obj)

        return post
class PostDetailSerializer(PostSerializer):
    """serializer for post details."""

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['content']



