from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_events(request):
    events = Event.objects.all().order_by('-created_at')
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_event(request, event_id):
    event = Event.objects.get(id=event_id)
    serializer = EventSerializer(event)

    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def get_ticket(request, event_id):
    response = {}
    response['status'] = 'Красный'

    qr_event_id = request.data['qr_event_id']
    qr_type = request.data['qr_type']
    qr_category = request.data['qr_category']
    qr_price = request.data['qr_price']

    if qr_event_id == event_id:
        event = Event.objects.get(id=event_id)
        try:
            ticket = Ticket.objects.get(user=request.user, event=event)
        except:
            ticket = Ticket.objects.create(
                user=request.user,
                event=event,
                type=qr_type,
                category=qr_category,
                price=qr_price,
                last_scan_time=timezone.now()
                )
            response['status'] = 'Зеленый'

        serializer = TicketSerializer(ticket)
        response['data'] = serializer.data

    else:
        response['status'] = 'Синий'

    return Response(response)
