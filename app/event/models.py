from django.db import models
from app.category.models import Category

class Event(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    start_at = models.DateTimeField()
    end_at_expected = models.DateTimeField()
    end_at_actual = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    score = models.FloatField(null=True, blank=True)

