"""
Tests for the Django admin modification.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Tests for the admin."""

    def setUp(self):
        """create a user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='password123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username='user',
            password='password123',
            email='user@example.com',
        )
