from rest_framework import serializers
from .models import Customer, CustomerVehicles


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = '__all__'


class CustomerVehiclesSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomerVehicles
        fields = '__all__'
