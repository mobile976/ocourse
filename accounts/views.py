from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import ProfileForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("course_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


class ProfileListView(ListView):
    model = Profile
    template_name = "accounts/profile_list.html"
    context_object_name = "profiles"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "accounts/profile_detail.html"
    context_object_name = "profile"


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_detail", pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile_form.html",
        {
            "form": form,
            "profile": profile,
        },
    )


def accounts_home(request):
    return render(request, "accounts/home.html")