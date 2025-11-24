from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
    )

    title = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)
    duration = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title