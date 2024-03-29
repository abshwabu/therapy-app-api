"""
Tests for Models.
"""
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(username='user', password='password123'):
    """create a new user"""
    return get_user_model().objects.create_user(username, password)


class ModelTest(TestCase):
    """Test models."""

    def test_create_user_successful(self):
        """Test creating a user is successful."""
        username = 'username'
        password = 'password123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'superuser',
            'password123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_community_post(self):
        """Test creating a community post."""
        user = get_user_model().objects.create_user(
            'username',
            'password123',
        )
        post = models.Post.objects.create(
            user=user,
            title='community post title',
            content='community post content',
        )

        self.assertEqual(str(post), post.title)

    def test_create_tag(self):
        """Test creating a tag is successful."""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='tag name')

        self.assertEqual(str(tag), tag.name)

    @patch('core.models.uuid.uuid4')
    def test_post_file_name_uuid(self, mock_uuid):
        """Test generating image patch."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.post_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads\\post\\{uuid}.jpg')
