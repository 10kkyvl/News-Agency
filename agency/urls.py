from django.urls import path

from agency.views import (
    NewsPaperListView,
    NewsPaperDetailView,
    CustomLoginView,
    SignUpView,
    CustomLogoutView
)


urlpatterns = [
    path("", NewsPaperListView.as_view(), name="newspaper-list"),
    path(
        "newspaper/<int:pk>", NewsPaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]

app_name = "agency"
