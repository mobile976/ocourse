from django.db import models


class CourseWish(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "Анхан шат"),
        ("intermediate", "Дунд шат"),
        ("advanced", "Ахисан шат"),
    ]

    title = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
    )
    desired_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        blank=True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
    )
    email = models.EmailField(
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("new", "Шинэ"),
            ("review", "Хянагдаж байна"),
            ("planned", "Төлөвлөсөн"),
            ("done", "Хийгдсэн"),
            ("rejected", "Хүлээж аваагүй"),
        ],
        default="new",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class CourseWishComment(models.Model):
    wish = models.ForeignKey(
        CourseWish,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=100, help_text="")
    email = models.EmailField(blank=True)
    text = models.TextField(help_text="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.name} on {self.wish}"