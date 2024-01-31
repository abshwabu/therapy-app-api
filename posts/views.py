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
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter post by user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')