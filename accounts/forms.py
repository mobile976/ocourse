from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Хэрэглэгчийн нэр",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "class": "form-control",
            "placeholder": "Хэрэглэгчийн нэрээ оруулна уу",
        })
    )
    password = forms.CharField(
        label="Нууц үг",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Нууц үгээ оруулна уу",
        }),
    )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Хэрэглэгчийн нэр"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Нууц үг"
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Нууц үг давтах"
            }),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_picture",
            "bio",
            "phone_number",
            "subscription_level",
            "social_links",
        ]

        labels = {
            "profile_picture": "Профайл зураг (URL)",
            "bio": "Товч намтар",
            "phone_number": "Утасны дугаар",
            "subscription_level": "Гишүүнчлэлийн түвшин",
            "social_links": "Социал линкүүд",
        }

        widgets = {
            "profile_picture": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/avatar.jpg",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Өөрийн тухай товч танилцуулга бичнэ үү...",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Жишээ: 88117773",
                }
            ),
            "subscription_level": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "social_links": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "Жишээ:\nhttps://facebook.com/username\nhttps://instagram.com/username",
                }
            ),
        }