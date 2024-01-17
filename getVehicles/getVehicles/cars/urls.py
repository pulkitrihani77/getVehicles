from django.contrib import admin
from django.urls import path
from . import views

app_name = "cars"
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:car_id>/',views.details,name="details"),
    path('add/',views.addCar,name="addCar"),
    path('delete/<int:car_id>/',views.deleteCar,name="deleteCar"),
    path('update/<int:car_id>/',views.updateCar,name="updateCar"),
]