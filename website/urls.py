import os

from django.conf import settings
from django.http import HttpResponse
from django.urls import path

from website.views import contact_view, dance_view, home_view, project_view


def robots_txt(request):
    path = os.path.join(settings.BASE_DIR, "website/static/website/robots.txt")
    with open(path) as f:
        return HttpResponse(f.read(), content_type="text/plain")


app_name = "website"

urlpatterns = [
    path("", home_view, name="home"),
    path("danser/", dance_view, name="dance"),
    path("projets/", project_view, name="project"),
    path("contact/", contact_view, name="contact"),
    path("robots.txt", robots_txt),
]
