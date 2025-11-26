# accounts/tests.py

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from .forms import (
    CustomAuthenticationForm,
    CustomUserCreationForm,
    ProfileForm,
)
from .models import Profile


class CustomUserCreationFormTests(TestCase):
    def test_valid_user_creation_form(self):
        form = CustomUserCreationForm(
            data={
                "username": "testuser",
                "password1": "StrongPass123",
                "password2": "StrongPass123",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_password_mismatch_is_invalid(self):
        form = CustomUserCreationForm(
            data={
                "username": "testuser",
                "password1": "StrongPass123",
                "password2": "WrongPass123",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_duplicate_username_is_invalid(self):
        User.objects.create_user(username="testuser", password="StrongPass123")

        form = CustomUserCreationForm(
            data={
                "username": "testuser",
                "password1": "AnotherStrong123",
                "password2": "AnotherStrong123",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)


class ProfileFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="profileuser",
            password="StrongPass123",
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_valid_profile_form(self):
        form = ProfileForm(
            instance=self.profile,
            data={
                "profile_picture": "https://example.com/avatar.jpg",
                "bio": "Энэ бол товч намтар.",
                "phone_number": "88117773",
                "subscription_level": "basic",
                "social_links": "https://facebook.com/user\nhttps://instagram.com/user",
            },
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_profile_picture_url(self):
        form = ProfileForm(
            instance=self.profile,
            data={
                "profile_picture": "not-a-valid-url",
                "bio": "Намтар",
                "phone_number": "88117773",
                "subscription_level": "free",
                "social_links": "",
            },
        )
        self.assertFalse(form.is_valid())
        self.assertIn("profile_picture", form.errors)

    def test_subscription_level_required_or_default(self):
        form = ProfileForm(
            instance=self.profile,
            data={
                "profile_picture": "",
                "bio": "",
                "phone_number": "",
                "subscription_level": "free",
                "social_links": "",
            },
        )
        self.assertTrue(form.is_valid(), form.errors)


class CustomAuthenticationFormTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="loginuser",
            password="StrongPass123",
        )

    def test_valid_login(self):
        request = self.factory.post("/accounts/login/")
        form = CustomAuthenticationForm(
            request,
            data={
                "username": "loginuser",
                "password": "StrongPass123",
            },
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_login_wrong_password(self):
        request = self.factory.post("/accounts/login/")
        form = CustomAuthenticationForm(
            request,
            data={
                "username": "loginuser",
                "password": "WrongPassword",
            },
        )
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn("__all__", form.errors)