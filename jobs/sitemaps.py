from django.contrib.sitemaps import Sitemap
from .models import Job

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.posted_at
