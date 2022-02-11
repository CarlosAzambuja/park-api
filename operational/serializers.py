from rest_framework import serializers
from .models import ParkMovement


class OperationalSerializer(serializers.ModelSerializer):

    class Meta:

        model = ParkMovement
        fields = '__all__'