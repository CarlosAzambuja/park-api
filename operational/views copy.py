from django.http import HttpResponse, JsonResponse

from customer.serializers import CustomerSerializer
from .models import ParkMovement
from .serializers import OperationalSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# CORS
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Operational index')


@csrf_exempt
def register(request, *args, **kwargs):
    if request.method == 'GET':
        park_movement = ParkMovement.objects.all()

        park_serializer = OperationalSerializer(
            park_movement, many=True)

        return JsonResponse(park_serializer.data, safe=False)

    elif request.method == "POST":
        park_data = JSONParser().parse(request)

        park_serializer = OperationalSerializer(data=park_data)

        if park_serializer.is_valid():
            park_serializer.save()
            return JsonResponse(park_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(park_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        park_movement = ParkMovement.objects.get(pk=kwargs.get('pk'))
    except:
        return JsonResponse({'message': 'ParkMovement doesnt exists'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        park_data = JSONParser().parse(request)
        park_serializer = OperationalSerializer(park_movement, data=park_data)
        if park_serializer.is_valid():
            park_serializer.save()
            return JsonResponse(park_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(park_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
