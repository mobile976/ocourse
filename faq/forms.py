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
            "question": "Асуулт*",
            "answer": "Хариулт*",
        }

    def clean_question(self):
        question = (self.cleaned_data.get("question") or "").strip()

        if len(question) < 5:
            raise forms.ValidationError("Асуулт дор хаяж 5 тэмдэгт байх ёстой.")

        qs = FAQ.objects.exclude(pk=self.instance.pk).filter(question__iexact=question)
        if qs.exists():
            raise forms.ValidationError("Ийм асуулттай Асуулт, хариулт аль хэдийн байна. Шаардлагатай бол хуучныг засварлана уу.")

        return question

    def clean_answer(self):
        answer = (self.cleaned_data.get("answer") or "").strip()

        if not answer:
            raise forms.ValidationError("Хариулт хоосон байж болохгүй.")

        if len(answer) < 10:
            raise forms.ValidationError("Хариулт арай дэлгэрэнгүй байхаар бичнэ үү (дор хаяж 10 тэмдэгт).")

        return answer


class FAQCommentForm(forms.ModelForm):
    class Meta:
        model = FAQComment
        fields = ["name", "email", "text"]

        labels = {
            "name": "Нэр*",
            "email": "И-мэйл",
            "text": "Сэтгэгдэл*",
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
                    "rows": 4,
                    "placeholder": "Сэтгэгдлээ энд бичнэ үү…",
                }
            ),
        }

    def clean_name(self):
        name = (self.cleaned_data.get("name") or "").strip()
        if not name:
            raise forms.ValidationError("Нэрээ заавал оруулна уу.")
        if len(name) < 2:
            raise forms.ValidationError("Нэр дор хаяж 2 тэмдэгт байх ёстой.")
        return name

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip()
        if not email:
            return ""
        return email

    def clean_text(self):
        text = (self.cleaned_data.get("text") or "").strip()
        if not text:
            raise forms.ValidationError("Сэтгэгдэл хоосон байж болохгүй.")
        if len(text) < 5:
            raise forms.ValidationError("Сэтгэгдлээ арай дэлгэрэнгүй бичнэ үү (дор хаяж 5 тэмдэгт).")
        return text