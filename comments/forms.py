from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
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
                    "placeholder": "Таны и-мэйл хаяг",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Сэтгэгдлээ энд бичнэ үү...",
                }
            ),
        }