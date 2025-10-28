from django.shortcuts import redirect, render
from rest_framework import viewsets
from .form.event_form import EventForm
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event/add_event.html', {'form': form})