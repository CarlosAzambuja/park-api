from django.db import models

from customer.models import CustomerVehicles

# Create your models here.


class ParkMovement(models.Model):
    entry_date = models.DateTimeField(null=True)
    exit_date = models.DateTimeField(null=True)
    validate_date = models.DateTimeField(null=True)
    value = models.FloatField(null=True)
    vehicle_id = models.ForeignKey(
        CustomerVehicles, on_delete=models.DO_NOTHING, related_name="vehicle", null=True)
