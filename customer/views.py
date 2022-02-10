from django.http import HttpResponse, JsonResponse
from .models import Customer, CustomerVehicles
from .serializers import CustomerSerializer, CustomerVehiclesSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# CORS
# from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Customer index.')


# @csrf_exempt
def register(request, *args, **kwargs):
    if request.method == 'GET':
        customers = Customer.objects.all()

        customerSerializer = CustomerSerializer(customers, many=True)

        return JsonResponse(customerSerializer.data, safe=False)

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        customer = Customer.objects.get(pk=kwargs.get('pk'))
    except:
        return JsonResponse({'message': 'Customer does not exists'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
def registerVehicle(request, *args, **kwargs):
    if request.method == 'GET':
        customers_vehicles = CustomerVehicles.objects.all()

        customer_vehicles_serializer = CustomerVehiclesSerializer(
            customers_vehicles, many=True)

        return JsonResponse(customer_vehicles_serializer.data, safe=False)

    elif request.method == 'POST':
        customer_vehicles_data = JSONParser().parse(request)
        customer_vehicles_serializer = CustomerVehiclesSerializer(
            data=customer_vehicles_data)
        if customer_vehicles_serializer.is_valid():
            customer_vehicles_serializer.save()
            return JsonResponse(customer_vehicles_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_vehicles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        customer_vehicles = CustomerVehicles.objects.get(pk=kwargs.get('pk'))
    except:
        return JsonResponse({'message': 'Customer does not exists'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        customer_vehicles_data = JSONParser().parse(request)
        customer_vehicles_serializer = CustomerVehiclesSerializer(
            customer_vehicles, data=customer_vehicles_data)
        if customer_vehicles_serializer.is_valid():
            customer_vehicles_serializer.save()
            return JsonResponse(customer_vehicles_serializer.data)
        return JsonResponse(customer_vehicles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
