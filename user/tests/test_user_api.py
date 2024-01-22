"""
Tests for the User API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


def create_user(**params):
    """Create a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserAPITest(TestCase):
    """Test for public api features."""

    def setUp(self):
        self.client = APIClient()

    