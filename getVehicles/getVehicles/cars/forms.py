from django import forms
from .models import allCars

class CarForm(forms.ModelForm):
    class Meta:
        model = allCars
        fields = ['car_name','car_desc','car_price','car_max_power','car_top_speed','car_image']
