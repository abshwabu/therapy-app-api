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

    def test_retrieve_tag(self):
        """Test retrieving tags"""
        Tag.objects.create(user=self.user, name='ADHD')
        Tag.objects.create(user=self.user, name='Anxiety')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-name')
        serializers = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializers.data)

    def test_tag_is_limited_to_user(self):
        """Test tag is limited to user"""
        tag = Tag.objects.create(user=self.user, name='Depression')
        user2 = get_user_model().objects.create_user(username='user2', password='password123')
        Tag.objects.create(user=user2, name='Bipolar')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
        self.assertEqual(res.data[0]['id'], tag.id)
