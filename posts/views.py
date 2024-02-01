"""
Views for post APIs.
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Post
from posts import serializers


class PostViewSet(viewsets.ModelViewSet):
    """view for manage post api."""
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter post by user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return serializer class for request."""
        if self.action == 'list':
            return serializers.PostSerializer

        else:
            return serializers.PostDetailSerializer

    def perform_create(self, serializer):
        """Create a new post."""
        serializer.save(user=self.request.user)