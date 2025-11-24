from django.contrib import admin
from .models import FAQ, FAQComment


class FAQCommentInline(admin.TabularInline):
    model = FAQComment
    extra = 0
    readonly_fields = ("name", "email", "text", "created_at")
    can_delete = True


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "author", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("question", "answer")
    inlines = [FAQCommentInline]


@admin.register(FAQComment)
class FAQCommentAdmin(admin.ModelAdmin):
    list_display = ("faq", "name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "text", "faq__question")