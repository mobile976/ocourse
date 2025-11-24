from django.urls import path
from . import views

urlpatterns = [
    path("", views.faq_list, name="faq_list"),
    path("my/", views.MyFAQListView.as_view(), name="my_faq_list"),
    path("create/", views.FAQCreateView.as_view(), name="faq_create"),
    path("<int:pk>/", views.faq_detail, name="faq_detail"),
    path("<int:pk>/edit/", views.FAQUpdateView.as_view(), name="faq_update"),
    path("<int:pk>/delete/", views.FAQDeleteView.as_view(), name="faq_delete"),
]