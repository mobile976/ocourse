from django.core.exceptions import ValidationError

def validate_youtube_url(value):
    if value and ("youtube.com" not in value and "youtu.be" not in value):
        raise ValidationError("Зөвхөн YouTube линк оруулна уу.")