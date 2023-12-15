from django.urls import path
from .views import Index, ReportCreateView, ReportUpdateView


urlpatterns = [
    path("", Index.as_view(), name="main_page"),
    path("add/", ReportCreateView.as_view(), name="create_page"),
    path("update/<int:pk>", ReportUpdateView.as_view(), name="edit_page"),
]
