from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "subscription_level", "phone_number", "created_at")
    list_filter = ("subscription_level", "created_at")
    search_fields = ("user__username", "user__email", "phone_number")

    def username(self, obj):
        return obj.user.username
    username.short_description = "User"
    username.admin_order_field = "user__username"