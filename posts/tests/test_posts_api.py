"""
Tests for post APIs.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Post

from posts.serializers import PostSerializer


POSTS_URL = reverse('post:post-list')

def create_post(user, **params):
    """Create and return a sample post."""
    defaults = {
        'title': 'sample title',
        'content': 'sample content'
    }
    defaults.update(params)

    post = Post.objects.create(user=user, **defaults)
    return post


class PublicPostAPITests(TestCase):
    """Testing unauthenticated api requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call api."""
        res = self.client.get(POSTS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivetPostAPITests(TestCase):
    """Test authenticated api requests"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'username',
            'password123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_post(self):
        """Test retrieving post."""
        create_post(user=self.user)
        create_post(user=self.user)

        res = self.client.get(POSTS_URL)

        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_post_is_limited_to_user(self):
        """Test list of posts is limited to the user."""
        other_user = get_user_model().objects.create_user(
            'other_user',
            'password123'
        )
        create_post(user=other_user)
        create_post(user=self.user)

        res = self.client.get(POSTS_URL)

        posts = Post.objects.filter(user=self.user)
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)