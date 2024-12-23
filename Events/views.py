from django.views.generic import TemplateView

# Create your views here.

class EventsPage(TemplateView):
    """
    Displays events page"
    """
    template_name = 'events/events.html'