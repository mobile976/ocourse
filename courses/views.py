from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from comments.forms import CommentForm
from courses.forms import CourseForm
from .models import Course, Category

class MyCoursesListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "courses/my_courses.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user).order_by("-created_at")

def course_list(request):
    category_slug = request.GET.get("category")

    courses = Course.objects.all()

    q = request.GET.get("q", "").strip()
    if q:
        from django.db.models import Q
        courses = courses.filter(
            Q(title__icontains=q)
            | Q(short_description__icontains=q)
            | Q(description__icontains=q)
        )

    order = request.GET.get("order", "")
    if order == "new":
        courses = courses.order_by("-created_at")
    elif order == "old":
        courses = courses.order_by("created_at")
    else:
        courses = courses.order_by("-created_at")

    duration = request.GET.get("duration", "")
    if duration == "short":
        courses = courses.order_by("duration")
    elif duration == "long":
        courses = courses.order_by("-duration")

    if category_slug:
        courses = courses.filter(category__slug=category_slug)

    categories = Category.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
        "selected_category": category_slug,
        "search_query": q,
        "selected_order": order,
        "selected_duration": duration,
    }

    return render(request, "courses/course_list.html", context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    comments = course.comments.order_by("-created_at")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.save()
            return redirect("course_detail", pk=course.pk)
    else:
        form = CommentForm()

    return render(
        request,
        "courses/course_detail.html",
        {
            "course": course,
            "comments": comments,
            "comment_form": form,
        },
    )

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user.is_authenticated and (obj.owner == user or user.is_superuser)


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    success_url = reverse_lazy("course_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

    def get_success_url(self):
        return reverse_lazy("course_detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/course_confirm_delete.html"
    success_url = reverse_lazy("course_list")