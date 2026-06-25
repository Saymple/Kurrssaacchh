from django.urls import path

from .views import home
from .views import car_detail
from .views import car_create
from .views import car_delete

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'car/<int:pk>/',
        car_detail,
        name='car_detail'
    ),

    path(
        'create/',
        car_create,
        name='create_car'
    ),

    path(
        'delete/<int:pk>/',
        car_delete,
        name='delete_car'
    ),
]