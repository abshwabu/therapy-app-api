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

    def test_user_list(self):
        """Test user are listed on the page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)
