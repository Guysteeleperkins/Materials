from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event_date'].widget.attrs.update({'id': 'event-datepicker'})

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'ticket_link', 'image', 'slug', 'status', 'event_date',]