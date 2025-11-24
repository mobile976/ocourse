from django.shortcuts import render
from .models import AboutPage


def about_view(request):
    about = AboutPage.objects.first()
    return render(request, "pages/about.html", {"about": about})