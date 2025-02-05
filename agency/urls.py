from django.urls import path

from agency.views import (
    NewsPaperListView,
    NewsPaperDetailView,
    CustomLoginView,
    SignUpView,
    CustomLogoutView,
    CreateTopicView,
    UpdateTopicView,
    DeleteTopicView,
    ProfileView
)


urlpatterns = [
    path("", NewsPaperListView.as_view(), name="newspaper-list"),
    path(
        "newspaper/<int:pk>", NewsPaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path("topic-create", CreateTopicView.as_view(), name="topic-create"),
    path(
        "topic-update/<int:pk>",
        UpdateTopicView.as_view(),
        name="topic-update"
    ),
    path(
        "topic-delete/<int:pk>",
        DeleteTopicView.as_view(),
        name="topic-delete"
    ),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]

app_name = "agency"
