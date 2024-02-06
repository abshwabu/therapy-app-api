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

    def _get_or_create_tags(self, tags, post):
        """Handles getting or creating a tag from a post."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            post.tags.add(tag_obj)

    def create(self, validated_data):
        """Create a new post."""
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        self._get_or_create_tags(tags, post)

        return post

    def update(self, instance, validated_data):
        """Update post."""
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
class PostDetailSerializer(PostSerializer):
    """serializer for post details."""

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['content']


class PostImageSerializer(serializers.ModelSerializer):
    """serializer for post images."""

    class Meta:
        model = Post
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
