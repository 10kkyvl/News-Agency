from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import DeleteView, UpdateView

from agency.forms import CustomUserCreationForm, TopicForm, ArticleForm
from agency.models import Newspaper, Redactor

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


class NewsPaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = ArticleForm
    template_name = "agency/forms/article_form.html"
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperEditView(LoginRequiredMixin, UpdateView):
    model = Newspaper
    form_class = ArticleForm
    template_name = "agency/forms/article_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "agency:newspaper-detail",
            kwargs={"pk": self.object.id}
        )


class NewsPaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper

    def get_success_url(self):
        return reverse_lazy(
            "agency:newspaper-detail",
            kwargs={"pk": self.object.id}
        )

class CreateTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "agency/forms/topic_form.html"
    success_url = reverse_lazy("agency:newspaper-list")


class UpdateTopicView(LoginRequiredMixin, UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "agency/forms/topic_form.html"
    success_url = reverse_lazy("agency:newspaper-list")


class DeleteTopicView(LoginRequiredMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:newspaper-list")


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


class EditorsList(ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    context_object_name = "editors"


class ProfileView(DetailView):
    model = Redactor
    context_object_name = "editor"
    template_name = "agency/redactor_profile.html"
