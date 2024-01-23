"""
Tests for the User API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


TOKEN_URL = reverse('user:token')


ME_URL = reverse('user:me')


def create_user(**params):
    """Create a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserAPITest(TestCase):
    """Test for public api features."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            'username': 'username',
            'password': 'password123',
            'email': 'user@example.com',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(username=payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_username_is_unique(self):
        """Test username is unique."""
        payload = {
            'username': 'username',
            'password': 'password123',
            'email': 'user@example.com',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test password is too short."""
        payload = {
            'username': 'username',
            'password': 'pwd',
            'email': 'user@example.com',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            username=payload['username']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test creating token for valid user"""
        user_details = {
            'username': 'username',
            'password': 'password123',
            'email': 'user@example.com',
        }
        create_user(**user_details)

        payload = {
            'username': user_details['username'],
            'password': user_details['password'],
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentials(self):
        """Test creating with invalid credentials."""
        create_user(username='username', password='password123')

        payload = {'username': 'username', 'password': 'password'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test creating with blank password."""
        payload = {'username': 'username', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthenticated(self):
        """Test authentication is required."""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivetUserApiTests(TestCase):
    """Tests for authenticated users."""

    def setUp(self):
        self.user = create_user(
            username='user',
            password='password123',
            email='user@example.com',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_user_success(self):
        """Test retrieve user is successful."""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'email': self.user.email,
            'username': self.user.username,
        })
