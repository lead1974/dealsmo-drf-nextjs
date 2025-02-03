"""
Tests for models.
"""
from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core_apps.users import models


def create_user(email='user@example.com', password='testpass123'):
    """Create a return a new user."""
    return get_user_model().objects.create_user(email, password)


class UserModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        username = 'testuser'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_valid_data(self):
        """Test creating a user with valid data is successful."""
        email = 'valid@example.com'
        password = 'validpass123'
        username = 'validuser'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.username, username)

    def test_user_email_uniqueness(self):
        """Test that creating a user with a duplicate email raises an error."""
        email = 'unique@example.com'
        password = 'uniquepass123'
        username = 'uniqueuser'
        get_user_model().objects.create_user(email=email, password=password, username=username)
        with self.assertRaises(Exception):
            get_user_model().objects.create_user(email=email, password='anotherpass', username='anotheruser')

    def test_user_username_uniqueness(self):
        """Test that creating a user with a duplicate username raises an error."""
        email = 'uniqueuser@example.com'
        password = 'uniquepass123'
        username = 'uniqueuser'
        get_user_model().objects.create_user(email=email, password=password, username=username)
        with self.assertRaises(Exception):
            get_user_model().objects.create_user(email='another@example.com', password='anotherpass', username=username)

    def test_username_validation(self):
        """Test that invalid usernames are rejected."""
        invalid_usernames = ['invalid user', 'invalid@user!', 'invalid/user']
        for username in invalid_usernames:
            user = get_user_model()(email='test@example.com', password='testpass123', username=username)
            with self.assertRaises(ValidationError):
                user.full_clean()

    def test_get_full_name(self):
        """Test the get_full_name property returns the correct full name."""
        user = get_user_model().objects.create_user(
            email='fullname@example.com',
            password='fullnamepass',
            username='fullnameuser',
            first_name='Full',
            last_name='Name'
        )
        self.assertEqual(user.get_full_name, 'Full Name')

    def test_required_fields(self):
        """Test that omitting required fields raises an error."""
        with self.assertRaises(Exception):
            get_user_model().objects.create_user(email='test@example.com', password='testpass123')

