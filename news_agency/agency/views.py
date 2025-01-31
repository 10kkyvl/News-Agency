from django.shortcuts import render
from django.views.generic import ListView, DetailView

from agency.models import Newspaper

from agency.models import Topic


class IndexView(ListView):
    paginate_by = 5
    model = Newspaper
    template_name = "agency/index.html"
    context_object_name = "newspapers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["topics"] = Topic.objects.all()

        return context

class NewsPaperDetailView(DetailView):
    model = Newspaper
    template_name = "agency/newspaper_detail.html"
    context_object_name = "newspaper"
