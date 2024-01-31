"""
Tests for recipe APIs.
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

        self.assertEqualL(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivetPostAPITests(TestCase):
    """Test authenticated api requests"""
