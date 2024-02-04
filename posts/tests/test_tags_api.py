"""
Tests for tags API.
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from posts.serializers import TagSerializer

TAGS_URL = reverse('post:tag-list')


def create_user(username='user', password='password123'):
    """create and return user."""
    return get_user_model().objects.create_user(username=username, password=password)


class PublicTagAPITest(TestCase):
    """Tests for unauthenticated api request."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Tests auth required for request."""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code,   status.HTTP_401_UNAUTHORIZED)


class PrivateTagAPITest(TestCase):
    """Tests for private api request."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        self.client.force_authenticate(self.user)
