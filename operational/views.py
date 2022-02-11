from django.http import HttpResponse, JsonResponse

from customer.serializers import CustomerSerializer, CustomerVehiclesSerializer
from .models import ParkMovement
from .serializers import OperationalSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import json

# CORS
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Operational index')


@csrf_exempt
def register(request, *args, **kwargs):
    if request.method == 'GET':
        movements = ParkMovement.objects.filter(exit_date__isnull=True)

        for movement in movements:
            data = {
                'id': movement.id,
                'plate': movement.vehicle_id.plate,
                'entry_date': movement.entry_date,
                'name': movement.vehicle_id.customer_id.name,
                'exit_date': movement.exit_date
            }

            return JsonResponse([data], safe=False)

    elif request.method == 'POST':
        ParkMovement.objects.create(
            entry_date = request.POST.get('entry_date'),
            value = request.POST.get('value')
        )
        # movement.entry_date = request.POST.get('entry_date')
        # movement.plate = request.POST.get('plate')

        # movement.save()
        
        return JsonResponse({'ok': 'true'})


