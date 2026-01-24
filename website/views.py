from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home_view(request):
    return render(request, "website/pages/page.html")


@require_GET
def dance_view(request):
    return render(request, "website/pages/danser/page.html")


@require_GET
def project_view(request):
    return render(request, "website/pages/projets/page.html")


@require_GET
def contact_view(request):
    return render(request, "website/pages/contact/page.html")
