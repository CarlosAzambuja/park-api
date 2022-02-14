from django.db import models

from customer.models import CustomerVehicles

# Create your models here.


class UpperCaseCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)


class ParkMovement(models.Model):
    plate = UpperCaseCharField(max_length=255, null=True)
    entry_date = models.DateTimeField(null=True)
    exit_date = models.DateTimeField(null=True)
    validate_date = models.DateTimeField(null=True)
    value = models.FloatField(null=True)
    vehicle_id = models.ForeignKey(
        CustomerVehicles, on_delete=models.DO_NOTHING, related_name="vehicle", null=True)
