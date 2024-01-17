from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from .models import allCars
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def index(request):
    searchLink = request.GET.get('searchCar')
    if(searchLink!='' and searchLink is not None):
        cars = allCars.objects.filter(Q(car_name__icontains=searchLink) | Q(car_desc__icontains=searchLink) | Q(car_max_power__icontains=searchLink) | Q(car_top_speed__icontains=searchLink))
        if not cars:
            messages.warning(request,f"No matching keyword for {searchLink}")
            cars = allCars.objects.all()
        else:
            messages.success(request,f"Following are results for {searchLink}")
    elif(searchLink == ''):
        messages.warning(request,f"Enter a valid Search...")
        cars = allCars.objects.all()
    else:
        cars = allCars.objects.all()
    return render(request,'cars/index.html',{'cars':cars})

def details(request,car_id):
    getCar = allCars.objects.get(pk=car_id)
    return render(request,'cars/cardetails.html',{'getCar':getCar})

@login_required
def addCar(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"New car added to the database, Thank You...")
        return redirect('cars:index')
    return render(request,'cars/form.html',{'form' : form})

@login_required
def deleteCar(request,car_id):
    getCar = allCars.objects.get(pk=car_id)

    if(request.POST):
        getCar.delete()
        messages.success(request,"Car deleted from the database...")
        return redirect('cars:index')
    return render(request,'cars/delete.html',{'getCar':getCar})

@login_required
def updateCar(request,car_id):
    getCar = allCars.objects.get(pk=car_id)
    form = CarForm(request.POST or None,instance=getCar)

    if form.is_valid():
        form.save()
        messages.success(request,"New Information updated...")
        return redirect('cars:index')
    return render(request,'cars/form_update.html',{'form' : form})

