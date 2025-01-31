from django.urls import path

from agency.views import (
    IndexView,
    NewsPaperDetailView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("newspaper/<int:pk>", NewsPaperDetailView.as_view(), name="newspaper-detail"),
]

app_name = "agency"
