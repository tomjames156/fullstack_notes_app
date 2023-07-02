from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]