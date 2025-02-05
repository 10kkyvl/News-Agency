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
    ProfileView,
    NewsPaperCreateView,
    NewsPaperEditView,
    NewsPaperDeleteView,
    EditorsList,
)


urlpatterns = [
    path("", NewsPaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>", NewsPaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspapers-create/",
        NewsPaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers-edit/<int:pk>",
        NewsPaperEditView.as_view(),
        name="newspaper-edit"
    ),
    path(
        "newspapers-delete/<int:pk>",
        NewsPaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path("topics-create", CreateTopicView.as_view(), name="topic-create"),
    path(
        "topics-update/<int:pk>",
        UpdateTopicView.as_view(),
        name="topic-update"
    ),
    path(
        "topics-delete/<int:pk>",
        DeleteTopicView.as_view(),
        name="topic-delete"
    ),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("editors/", EditorsList.as_view(), name="editors"),
    path("profiles/<int:pk>", ProfileView.as_view(), name="profile"),
]

app_name = "agency"
