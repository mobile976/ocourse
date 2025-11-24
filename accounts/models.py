from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    SUBSCRIPTION_CHOICES = [
        ("free", "Сонирхогч"),
        ("student", "Сурагч"),
        ("teacher", "Багш"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        help_text="Зургийн URL оруулна уу"
    )
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subscription_level = models.CharField(
        max_length=20,
        choices=SUBSCRIPTION_CHOICES,
        default="free",
    )
    social_links = models.TextField(
        blank=True,
        help_text="Нэг мөрөнд нэг URL бичнэ үү.",
    )

    def __str__(self):
        return f"Profile of {self.user.username}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()