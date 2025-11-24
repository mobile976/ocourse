# student/tests.py
from django.test import TestCase
from .forms import CourseWishForm, CourseWishCommentForm
from .models import CourseWish

class CourseWishFormTests(TestCase):
    def test_valid_data(self):
        """Бүх талбар зөв бөглөгдвөл form хүчинтэй байх ёстой."""
        form = CourseWishForm(
            data={
                "title": "Python анхан шат",
                "description": "Анхан шатны Python хичээл байгаасай.",
                "desired_level": "beginner",
                "name": "Бат",
                "email": "bat@example.com",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_title_is_required(self):
        """title хоосон бол form буруу байх ёстой (CharField blank=False)."""
        form = CourseWishForm(
            data={
                "title": "",
                "description": "Дэлгэрэнгүй тайлбар байна.",
                "desired_level": "intermediate",
                "name": "Бат",
                "email": "bat@example.com",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_optional_fields_can_be_blank(self):
        """
        description, desired_level, name, email бүгд хоосон байж болно,
        зөвхөн title бөглөхөд form хүчинтэй байх ёстой.
        """
        form = CourseWishForm(
            data={
                "title": "Django advanced",
                "description": "",
                "desired_level": "",
                "name": "",
                "email": "",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)


class CourseWishCommentFormTests(TestCase):
    def test_valid_comment_minimal(self):
        """Нэр + сэтгэгдэл байхад, и-мэйл хоосон ч form хүчинтэй."""
        form = CourseWishCommentForm(
            data={
                "name": "Сараа",
                "email": "",
                "text": "Энэ санаа их таалагдлаа.",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_name_is_required(self):
        """name хоосон бол form хүчинтэй биш байх ёстой."""
        form = CourseWishCommentForm(
            data={
                "name": "",
                "email": "test@example.com",
                "text": "Сэтгэгдэл байна.",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_text_is_required(self):
        """text (сэтгэгдэл) хоосон бол form хүчинтэй биш."""
        form = CourseWishCommentForm(
            data={
                "name": "Сараа",
                "email": "test@example.com",
                "text": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("text", form.errors)

    def test_email_optional(self):
        """И-мэйл хоосон байж болно."""
        form = CourseWishCommentForm(
            data={
                "name": "Тэмүүжин",
                "email": "",
                "text": "И-мэйл үлдээхгүй ч болно.",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)