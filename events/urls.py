from . import views
from django.urls import path

urlpatterns = [
    path('events', views.EventsPage.as_view(), name='events'),
    path('addevent', views.AddEvent.as_view(), name='addevent'),
]