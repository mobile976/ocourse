from django.test import TestCase
from .forms import CommentForm


class CommentFormTests(TestCase):
    def test_form_valid_with_all_fields(self):
        """Нэр, зөв и-мэйл, сэтгэгдэл гурвуулаа байхад form хүчинтэй байх ёстой."""
        form = CommentForm(
            data={
                "name": "Test User",
                "email": "user@example.com",
                "text": "Энэ бол тест сэтгэгдэл.",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_without_name(self):
        """Нэр оруулаагүй үед form хүчинтэй биш байх ёстой."""
        form = CommentForm(
            data={
                "name": "",
                "email": "user@example.com",
                "text": "Сайн байна уу?",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_form_invalid_without_text(self):
        """Сэтгэгдэл хоосон үед form хүчинтэй биш байх ёстой."""
        form = CommentForm(
            data={
                "name": "Test User",
                "email": "user@example.com",
                "text": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("text", form.errors)

    def test_form_invalid_with_bad_email(self):
        """И-мэйл буруу форматтай үед form хүчинтэй биш байх ёстой."""
        form = CommentForm(
            data={
                "name": "Test User",
                "email": "not-an-email",
                "text": "Сэтгэгдэлтэй холбоотой текст.",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)