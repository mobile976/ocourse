from django.db import models
from django.conf import settings


class FAQ(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="faqs",
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.question


class FAQComment(models.Model):
    faq = models.ForeignKey(
        FAQ,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.name} on {self.faq}"