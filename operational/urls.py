
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="vehicle_register"),
    path('register/<int:pk>', views.register, name="vehicle_register")
]
