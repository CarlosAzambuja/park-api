from django.db import models

from customer.models import CustomerVehicles

# Create your models here.
class ParkMovement(models.Model):
    entry_date = models.DateField()
    exit_date = models.DateField()
    validate_date = models.DateField()
    value = models.FloatField()
    vehicle_id = models.ForeignKey(CustomerVehicles, on_delete=models.DO_NOTHING)

