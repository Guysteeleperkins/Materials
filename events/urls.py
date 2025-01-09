from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('add-event/', views.AddEvent.as_view(), name='add-event'),
]