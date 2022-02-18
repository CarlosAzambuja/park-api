from django.http import HttpResponse, JsonResponse
from customer.models import CustomerVehicles

from .models import ParkMovement
from rest_framework import status
import json

# CORS
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Operational index')


def get(request):
    movements = ParkMovement.objects.filter(exit_date__isnull=True)
    list_data = []

    for movement in movements:
        name = ''
        plate = ''
        entry_date = ''
        exit_date = ''

        if movement.vehicle_id:
            plate = movement.vehicle_id.plate

        if movement.vehicle_id and movement.vehicle_id.customer_id:
            name = movement.vehicle_id.customer_id.name

        if movement.entry_date:
            entry_date = movement.entry_date

        if movement.exit_date:
            exit_date = movement.exit_date

        data = {
            'id': movement.id,
            'plate': plate,
            'entry_date': entry_date,
            'name': name,
            'exit_date': exit_date
        }

        list_data.append(data)

    return JsonResponse(list_data, safe=False)


@csrf_exempt
def register(request, *args, **kwargs):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    if data['plate']:
        vehicle = CustomerVehicles.objects.filter(
            plate=data['plate']).first()

    if not vehicle:
        vehicle_id = CustomerVehicles.objects.create(
            plate=data['plate']
        ).id
    else:
        vehicle_id = vehicle.id

    checkMovement = ParkMovement.objects.filter(
        plate=data['plate'].upper(), exit_date__isnull=True)

    if not checkMovement:
        ParkMovement.objects.create(
            entry_date=data['entry_date'],
            plate=data['plate'],
            vehicle_id_id=vehicle_id
        )

        return JsonResponse(data, status=status.HTTP_201_CREATED, safe=False)
    return JsonResponse(data, status=status.HTTP_409_CONFLICT, safe=False)


@csrf_exempt
def update(request, *args, **kwargs):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    ParkMovement.objects.filter(id=kwargs['pk']).update(exit_date=data)

    return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
