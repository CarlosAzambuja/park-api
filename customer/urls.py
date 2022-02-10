
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="customer_register"),
    path('register/<int:pk>', views.register, name="customer_edit"),
    path('registervehicle', views.registerVehicle, name="vehicle_register"),
    path('registervehicle/<int:pk>', views.registerVehicle, name="vehicle_edit")
]
