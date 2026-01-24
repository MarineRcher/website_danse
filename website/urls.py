from django.urls import path

from website.views import contact_view, dance_view, home_view, project_view

app_name = "website"

urlpatterns = [
    path("", home_view, name="home"),
    path("danser/", dance_view, name="dance"),
    path("projets/", project_view, name="project"),
    path("contact/", contact_view, name="contact"),
]
