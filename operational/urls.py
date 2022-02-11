
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('movement/register', views.register, name="park_movement_register"),
    path('movement/register/<int:pk>', views.register, name="park_movement_edit")
]
