from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import CourseWish
from .forms import CourseWishForm, CourseWishCommentForm


class CourseWishListView(ListView):
    model = CourseWish
    template_name = "student/wish_list.html"
    context_object_name = "wishes"
    paginate_by = 10

    def get_queryset(self):
        return CourseWish.objects.exclude(status="rejected").order_by("-created_at")


class CourseWishCreateView(CreateView):
    model = CourseWish
    form_class = CourseWishForm
    template_name = "student/wish_form.html"
    success_url = reverse_lazy("wish_list")


def course_wish_detail(request, pk):
    wish = get_object_or_404(CourseWish, pk=pk)
    comments = wish.comments.all()

    if request.method == "POST":
        form = CourseWishCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.wish = wish
            comment.save()
            return redirect("wish_detail", pk=wish.pk)
    else:
        form = CourseWishCommentForm()

    return render(
        request,
        "student/wish_detail.html",
        {
            "wish": wish,
            "comments": comments,
            "form": form,
        },
    )