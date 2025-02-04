from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import RedirectView

from agency.forms import CustomUserCreationForm
from agency.models import Newspaper

from agency.models import Topic


class NewsPaperListView(ListView):
    paginate_by = 5
    model = Newspaper
    template_name = "agency/newspaper_list.html"
    context_object_name = "newspapers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["topics"] = Topic.objects.all()

        return context


class NewsPaperDetailView(DetailView):
    model = Newspaper
    template_name = "agency/newspaper_detail.html"
    context_object_name = "newspaper"


class CustomLoginView(LoginView):
    template_name = "agency/forms/login_form.html"
    success_url = reverse_lazy("agency:newspaper-list")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "agency/registration/signup.html"
    success_url = reverse_lazy("agency:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class CustomLogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy("agency:newspaper-list")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
