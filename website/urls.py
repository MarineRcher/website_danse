from django.urls import path

from website.views import (
    home_view,
)

app_name = "website"

urlpatterns = [
    path("", home_view, name="home"),
]
