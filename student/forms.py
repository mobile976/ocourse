from django import forms
from .models import CourseWish, CourseWishComment


class CourseWishForm(forms.ModelForm):
    class Meta:
        model = CourseWish
        fields = ["title", "description", "desired_level", "name", "email"]

        labels = {
            "title": "Сэдэв",
            "description": "Тайлбар",
            "desired_level": "Хүсэж буй түвшин",
            "name": "Таны нэр",
            "email": "И-мэйл",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Жишээ: Python эхлэнэ, Англи хэлний дүрэм...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Дэлгэрэнгүй бичээрэй...",
                }
            ),
            "desired_level": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Нэр",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "И-мэйл",
                }
            ),
        }


class CourseWishCommentForm(forms.ModelForm):
    class Meta:
        model = CourseWishComment
        fields = ["name", "email", "text"]

        labels = {
            "name": "Нэр",
            "email": "И-мэйл",
            "text": "Сэтгэгдэл",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Таны нэр",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Таны и-мэйл",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Сэтгэгдлээ энд бичнэ үү…",
                }
            ),
        }