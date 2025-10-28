from django.db import models

from app.event.models import Event


class Option(models.Model):
    name = models.CharField(max_length=255)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='options')
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
