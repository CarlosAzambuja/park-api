from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerVehicles

admin.site.register({
    Customer,
    CustomerVehicles
})
