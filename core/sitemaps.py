from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ["website:home", "website:dance", "website:project", "website:contact"]

    def location(self, item):
        return reverse(item)
