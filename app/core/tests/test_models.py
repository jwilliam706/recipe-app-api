from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='sample@email.com', password='testpassword'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan',
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_srt(self):
        """Testing the ingredients string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
