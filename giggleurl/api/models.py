import uuid

from django.db import models
from django.utils import timezone


class Url(models.Model):
    url = models.CharField(primary_key=True, max_length=200)
    original_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
