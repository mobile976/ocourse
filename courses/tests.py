# courses/tests.py

from django.test import TestCase
from .forms import CourseForm
from .models import Category


class CourseFormTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Programming",
            slug="programming",
        )

    def _base_valid_data(self, **overrides):
        """
        Давтагдах код багасгахын тулд нэг үндсэн dict гаргаад
        хэрэгтэй үед нь override хийж ашиглая.
        """
        data = {
            "title": "Django эхлэл",
            "image_url": "https://example.com/image.jpg",
            "duration": "3 долоо хоног",
            "short_description": "Django-гийн анхан шатны хичээл.",
            "description": "Энэ хичээлээр Django-гийн үндсэн ойлголтыг судална.",
            "video_url": "https://www.youtube.com/watch?v=123456",
            "category": self.category.pk,
        }
        data.update(overrides)
        return data

    def test_form_valid_with_correct_data(self):
        """Бүх өгөгдөл зөв үед form хүчинтэй байх ёстой."""
        form = CourseForm(data=self._base_valid_data())
        self.assertTrue(form.is_valid(), form.errors)

    def test_title_is_required(self):
        """title хоосон үед алдаа өгөх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(title="  ")
        )
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("Хичээлийн нэрийг заавал оруулна уу.", form.errors["title"][0])

    def test_title_min_length(self):
        """title хамгийн багадаа 3 тэмдэгт байх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(title="Dj")
        )
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("хамгийн багадаа 3 тэмдэгт", form.errors["title"][0])

    def test_video_url_allows_youtube(self):
        """YouTube domain-тай линк зөвшөөрөгдөх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(video_url="https://www.youtube.com/watch?v=abc123")
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_video_url_allows_youtu_be(self):
        """youtu.be богино линк зөвшөөрөгдөх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(video_url="https://youtu.be/abc123")
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_video_url_allows_vimeo(self):
        """vimeo.com линк зөвшөөрөгдөх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(video_url="https://vimeo.com/123456")
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_video_url_invalid_domain(self):
        """video_url нь өөр домэйнтэй бол алдаа өгөх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(video_url="https://example.com/video.mp4")
        )
        self.assertFalse(form.is_valid())
        self.assertIn("video_url", form.errors)
        self.assertIn("YouTube эсвэл Vimeo линк", form.errors["video_url"][0])

    def test_description_required_if_video_given(self):
        """Видео линк байвал description заавал байх ёстой."""
        form = CourseForm(
            data=self._base_valid_data(description="   ")
        )
        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors)
        self.assertIn("Видео оруулсан бол хичээлийн дэлгэрэнгүй тайлбарыг заавал бичнэ үү.",
                      form.errors["description"][0])

    def test_no_video_no_description_is_ok(self):
        """Видео байхгүй бол description заавал биш (формын clean-тэй зөрчилдөхгүй байхыг шалгах)."""
        form = CourseForm(
            data=self._base_valid_data(video_url="", description="")
        )
        self.assertTrue(form.is_valid(), form.errors)