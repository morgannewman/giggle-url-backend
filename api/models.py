import uuid

from django.db import models
from django.utils import timezone
from word_service import get_next_giggle


class Url(models.Model):
    giggle = models.CharField(primary_key=True, max_length=72, default=get_next_giggle)
    url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)

