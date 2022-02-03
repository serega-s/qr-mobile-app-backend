from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Event, Ticket


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['name', 'description', 'date', 'start_time', 'end_time']
    list_filter = ['customer', 'enter_name', 'date']
    search_fields = ['name', 'customer', 'description']
    ordering = ['-created_at']


admin.site.register(Ticket)
