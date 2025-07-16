from django.db import models

class Job(models.Model):
    JOB_TYPES = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    region = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    category = models.CharField(max_length=100)
    description = models.TextField()
    apply_link = models.URLField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.job.title}"
