from django.urls import path
from .views import Index, ReportCreateView


urlpatterns = [
    path("", Index.as_view()),
    path("add/", ReportCreateView.as_view()),
]
