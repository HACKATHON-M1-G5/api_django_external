from django import forms
from app.event.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['category', 'name', 'start_at', 'end_at_expected', 'end_at_actual', 'status', 'score']
