from django.db import models
from courses.models import Course


class Comment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.course.title}"