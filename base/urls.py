from django.urls import path

from . import views

urlpatterns = [
    path('events_ticket/<int:event_id>/', views.get_ticket),
    path('events/', views.get_events),
    path('events/<int:event_id>/', views.get_event),
]
