from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Event

# Create your views here.

class EventsPage(TemplateView):
    """
    Displays events page"
    """
    template_name = 'events/events.html'


def events_page(request):
    events = Event.objects.all().order_by('event_date')  # Fetch all events
    return render(request, 'events.html', {'events': events})

class AddEvent(TemplateView):
    """
    Displays events page"
    """
    template_name = 'events/addevent.html'