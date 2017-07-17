from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    OPEN = 0
    SKIPPED = 1
    SHARED = 2
    STATUSES = (
        (OPEN, 'Open'),
        (SKIPPED, 'Skipped'),
        (SHARED, 'Shared'),
    )

    title = models.CharField(max_length=300, unique=True)
    url = models.CharField(max_length=200, unique=True)
    summary = models.TextField(blank=True, null=True)
    published = models.DateTimeField(null=True)
    status = models.IntegerField(
        choices=STATUSES,
        default=OPEN,
    )

    edited = models.DateTimeField(auto_now=True)
    # TODO: populate when we have login
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
