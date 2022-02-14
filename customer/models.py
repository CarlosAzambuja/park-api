from django.db import models
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


class Customer(models.Model):
    name = models.CharField(max_length=50)


class CustomerVehicles(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    plate = UpperCaseCharField(max_length=10)
    kind = models.IntegerField(choices=[(1, 'MOTO'), [2, 'CARRO']], null=True)
