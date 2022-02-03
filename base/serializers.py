from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Event, Ticket

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = [
            'created_at'
        ]


class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ticket
