from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    path("", views.accounts_home, name="accounts_home"),
    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=CustomAuthenticationForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page="course_list"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    path("profiles/", views.ProfileListView.as_view(), name="profile_list"),
    path("profiles/<int:pk>/", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/edit/", views.edit_profile, name="profile_edit"),
]