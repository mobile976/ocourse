from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import FAQ
from .forms import FAQForm, FAQCommentForm


def faq_list(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, "faq/faq_list.html", {"faqs": faqs})


def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk, is_active=True)
    comments = faq.comments.all()

    if request.method == "POST":
        form = FAQCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.faq = faq
            comment.save()
            return redirect("faq_detail", pk=faq.pk)
    else:
        form = FAQCommentForm()

    return render(
        request,
        "faq/faq_detail.html",
        {
            "faq": faq,
            "comments": comments,
            "form": form,
        },
    )


class MyFAQListView(LoginRequiredMixin, ListView):
    model = FAQ
    template_name = "faq/my_faq_list.html"
    context_object_name = "faqs"

    def get_queryset(self):
        return FAQ.objects.filter(author=self.request.user)


class FAQOwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user.is_authenticated and (obj.author == user or user.is_superuser)


class FAQCreateView(LoginRequiredMixin, CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = "faq/faq_form.html"
    success_url = reverse_lazy("faq_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FAQUpdateView(LoginRequiredMixin, FAQOwnerRequiredMixin, UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = "faq/faq_form.html"

    def get_success_url(self):
        return reverse_lazy("my_faq_list")


class FAQDeleteView(LoginRequiredMixin, FAQOwnerRequiredMixin, DeleteView):
    model = FAQ
    template_name = "faq/faq_confirm_delete.html"
    success_url = reverse_lazy("my_faq_list")