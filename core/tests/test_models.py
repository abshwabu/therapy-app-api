"""
Tests for Models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


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
