from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseWishListView.as_view(), name="wish_list"),
    path("create/", views.CourseWishCreateView.as_view(), name="wish_create"),
    path("<int:pk>/", views.course_wish_detail, name="wish_detail"),
]