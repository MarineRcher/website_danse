from django.urls import path

from website.views import dance_view, home_view

app_name = "website"

urlpatterns = [
    path("", home_view, name="home"),
    path("danser/", dance_view, name="dance"),
]
