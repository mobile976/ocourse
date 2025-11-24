from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("create/", views.CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/", views.course_detail, name="course_detail"),
    path("<int:pk>/edit/", views.CourseUpdateView.as_view(), name="course_update"),
    path("<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course_delete"),
    path("my-courses/", views.MyCoursesListView.as_view(), name="my_courses"),
]