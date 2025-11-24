from django.contrib import admin
from .models import CourseWish, CourseWishComment


class CourseWishCommentInline(admin.TabularInline):
    model = CourseWishComment
    extra = 0
    readonly_fields = ("name", "email", "text", "created_at")


@admin.register(CourseWish)
class CourseWishAdmin(admin.ModelAdmin):
    list_display = ("title", "desired_level", "status", "created_at", "name", "email")
    list_filter = ("status", "desired_level", "created_at")
    search_fields = ("title", "description", "name", "email")
    inlines = [CourseWishCommentInline]


@admin.register(CourseWishComment)
class CourseWishCommentAdmin(admin.ModelAdmin):
    list_display = ("wish", "name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "text", "wish__title")