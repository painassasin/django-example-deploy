from django.db import IntegrityError
from django.test import TestCase

from users.models import User


class TestUserModel(TestCase):
    def test_have_to_create_user_with_email_only(self):
        email = 'test@example.com'

        user = User.objects.create_user(email=email)

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.has_usable_password())

    def test_have_to_create_user_with_password(self):
        email, password = 'test@example.com', 'secret-value'

        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertNotEqual(user.password, password)
        self.assertTrue(user.check_password(password))

    def test_have_to_create_superuser_with_permissions(self):
        user = User.objects.create_superuser(email='admin@example.com')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_failed_to_create_user_with_existing_email(self):
        common_email = 'test@example.com'
        User.objects.create_user(email=common_email)

        with self.assertRaises(IntegrityError):
            User.objects.create_user(email=common_email)

    def test_failed_to_create_user_with_empty_email(self):
        with self.assertRaisesMessage(ValueError, 'Users must have an email address'):
            User.objects.create_user(email='')

    def test_user_to_string(self):
        user = User.objects.create_user(email='test@example.com')
        self.assertEqual(str(user), 'User(email=test@example.com)')
