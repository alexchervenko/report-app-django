from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from .models import Report


# Create your views here.


class Index(View):
    def get(self, request):
        boards_to_repair = Report.objects.filter(status__exact="need_repair")
        not_tested_boards = Report.objects.filter(status__exact="not_tested")
        return render(
            request,
            template_name="index.html",
            context={
                "not_tested_boards": not_tested_boards,
                "boards_to_repair": boards_to_repair,
            },
        )


class ReportCreateView(CreateView):
    model = Report
    fields = "__all__"
    template_name = "reports/report_form.html"
    success_url = "/reports"


class ReportUpdateView(UpdateView):
    model = Report
    fields = "__all__"
    template_name = "reports/report_form.html"
    success_url = "/reports"
