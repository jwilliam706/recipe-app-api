from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating a new user with an email is successful"""
        user = get_user_model().objects.create_user(
            email="email@example.com", password="pass123"
        )
        self.assertEqual(user.email, "email@example.com")
        self.assertTrue(user.check_password("pass123"))

    def test_create_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        user = get_user_model().objects.create_user(
            email="email@DOMAIN.COM", password="pass123"
        )
        self.assertEqual(user.email, "email@DOMAIN.COM".lower())

    def test_new_user_invalid_email(self):
        """Creating a user without providing and email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_super(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@super.com", "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
