from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "title",
            "image_url",
            "duration",
            "short_description",
            "description",
            "video_url",
            "category",
        ]

        labels = {
            "title": "Хичээлийн нэр",
            "image_url": "Зургийн URL",
            "duration": "Хугацаа",
            "short_description": "Товч тайлбар",
            "description": "Дэлгэрэнгүй тайлбар",
            "video_url": "Видео URL",
            "category": "Ангилал",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Жишээ: Django эхлэл, Python анхан шат...",
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Жишээ: https://example.com/image.jpg",
                }
            ),
            "duration": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Жишээ: 3 долоо хоног, 12 цаг, 8 хичээл...",
                }
            ),
            "short_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "Хичээлийн товч танилцуулгыг бичнэ үү...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Дэлгэрэнгүй тайлбар бичнэ үү...",
                }
            ),
            "video_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "YouTube / Vimeo линк...",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }