
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('customer/register', views.register, name="customer_register"),
    path('customer/register/<int:pk>', views.register, name="customer_edit"),
    path('vehicle/register', views.registerVehicle, name="vehicle_register"),
    path('vehicle/register/<int:pk>', views.registerVehicle, name="vehicle_edit")
]
