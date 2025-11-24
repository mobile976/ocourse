# faq/tests.py

from django.test import TestCase
from .forms import FAQForm, FAQCommentForm
from .models import FAQ


class FAQFormTests(TestCase):
    def setUp(self):
        self.existing_faq = FAQ.objects.create(
            question="Django хэрхэн суулгах вэ?",
            answer="Django-г pip ашиглан суулгаж болно.",
        )

    def test_valid_faq_form(self):
        """Зөв асуулт, хариулт өгвөл form хүчинтэй байх ёстой."""
        form = FAQForm(
            data={
                "question": "Python гэж юу вэ?",
                "answer": "Python нь олон талт, өндөр түвшний програмчлалын хэл.",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_question_too_short(self):
        """Асуултын урт < 5 бол алдаа өгөх ёстой."""
        form = FAQForm(
            data={
                "question": "Сайн",
                "answer": "Хариулт нь хангалттай урт байна.",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("question", form.errors)
        self.assertIn("дор хаяж 5 тэмдэгт", form.errors["question"][0])

    def test_duplicate_question_case_insensitive(self):
        """Ижил асуулт (том/жижиг үсэг үл хамааран) байвал алдаа өгөх ёстой."""
        form = FAQForm(
            data={
                "question": "django хэрхэн суулгах вэ?",
                "answer": "Шинэ хариулт.",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("question", form.errors)
        self.assertIn("аль хэдийн байна", form.errors["question"][0])

    def test_empty_answer_not_allowed(self):
        """Хариулт хоосон бол алдаа."""
        form = FAQForm(
            data={
                "question": "Шинэ асуулт байна уу?",
                "answer": "   ",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("answer", form.errors)
        self.assertIn("хоосон байж болохгүй", form.errors["answer"][0])

    def test_answer_too_short(self):
        """Хариултын урт < 10 бол алдаа."""
        form = FAQForm(
            data={
                "question": "Шинэ асуулт байна уу?",
                "answer": "Богино",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("answer", form.errors)
        self.assertIn("дор хаяж 10 тэмдэгт", form.errors["answer"][0])

    def test_update_same_question_is_allowed(self):
        """
        Өөрийн instance-ээ update хийх үед,
        асуулт нь өөрчлөгдөөгүй байвал давхардлын алдаа гарах ёсгүй.
        """
        form = FAQForm(
            data={
                "question": self.existing_faq.question,
                "answer": "Хариултыг шинэчиллээ.",
            },
            instance=self.existing_faq,
        )
        self.assertTrue(form.is_valid(), form.errors)


class FAQCommentFormTests(TestCase):
    def test_valid_comment_form_minimal(self):
        """Зөв нэр + хангалттай урт сэтгэгдэлтэй, и-мэйл хоосон байж болно."""
        form = FAQCommentForm(
            data={
                "name": "Бат",
                "email": "",
                "text": "Энэ бол ашигтай мэдээлэл байна.",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_name_required(self):
        """Нэр хоосон бол алдаа."""
        form = FAQCommentForm(
            data={
                "name": "   ",
                "email": "test@example.com",
                "text": "Сэтгэгдэл байна.",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("Нэрээ заавал оруулна уу.", form.errors["name"][0])

    def test_name_min_length(self):
        """Нэрийн урт < 2 бол алдаа."""
        form = FAQCommentForm(
            data={
                "name": "А",
                "email": "test@example.com",
                "text": "Сэтгэгдэл байна.",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("дор хаяж 2 тэмдэгт", form.errors["name"][0])

    def test_email_optional(self):
        """И-мэйл оруулаагүй ч form хүчинтэй байх ёстой."""
        form = FAQCommentForm(
            data={
                "name": "Бат",
                "email": "   ",
                "text": "Сэтгэгдэл байна.",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)
        cleaned = form.clean()
        self.assertEqual(cleaned["email"], "")

    def test_text_required(self):
        """Сэтгэгдэл хоосон байж болохгүй."""
        form = FAQCommentForm(
            data={
                "name": "Бат",
                "email": "test@example.com",
                "text": "   ",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("text", form.errors)
        self.assertIn("хоосон байж болохгүй", form.errors["text"][0])

    def test_text_min_length(self):
        """Сэтгэгдэл дор хаяж 5 тэмдэгт байх ёстой."""
        form = FAQCommentForm(
            data={
                "name": "Бат",
                "email": "test@example.com",
                "text": "Hi!",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("text", form.errors)
        self.assertIn("дор хаяж 5 тэмдэгт", form.errors["text"][0])