
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('movement/get', views.get, name="park_movement_get"),
    path('movement/register', views.register, name="park_movement_register"),
    path('movement/update/<int:pk>', views.update, name="park_movement_edit")
]
