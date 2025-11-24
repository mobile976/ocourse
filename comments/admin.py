from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("course", "name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "text")