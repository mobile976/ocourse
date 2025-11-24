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

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Хичээлийн нэрийг заавал оруулна уу.")
        if len(title) < 3:
            raise forms.ValidationError("Хичээлийн нэр хамгийн багадаа 3 тэмдэгт байна.")
        return title

    def clean_video_url(self):
        url = self.cleaned_data.get("video_url")

        if not url:
            return url

        allowed_domains = ["youtube.com", "youtu.be", "vimeo.com"]
        if not any(domain in url for domain in allowed_domains):
            raise forms.ValidationError(
                "Видео URL нь YouTube эсвэл Vimeo линк байх ёстой."
            )

        return url

    def clean(self):
        cleaned_data = super().clean()
        video_url = cleaned_data.get("video_url")
        description = cleaned_data.get("description", "").strip()

        if video_url and not description:
            self.add_error(
                "description",
                "Видео оруулсан бол хичээлийн дэлгэрэнгүй тайлбарыг заавал бичнэ үү.",
            )

        return cleaned_data