from django import forms
from .models import FAQ, FAQComment


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ["question", "answer"]
        widgets = {
            "question": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Асуултаа бичнэ үү…",
                }
            ),
            "answer": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Энд дэлгэрэнгүй хариултаа бичнэ үү…",
                }
            ),
        }
        labels = {
            "question": "Асуулт",
            "answer": "Хариулт",
        }


class FAQCommentForm(forms.ModelForm):
    class Meta:
        model = FAQComment
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
                    "placeholder": "Таны и-мэйл (шаардлагатай бол)",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Сэтгэгдлээ энд бичнэ үү…",
                }
            ),
        }