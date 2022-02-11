from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)


class CustomerVehicles(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    plate = models.CharField(max_length=10)
    kind = models.IntegerField(choices = [(1, 'MOTO'), [2, 'CARRO']], null=True)
