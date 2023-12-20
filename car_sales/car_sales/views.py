from django.shortcuts import render,redirect
from car.models import *

def home(request,slug_type=None):
    data = car.objects.all()
    if slug_type is not None:
        br = brand.objects.get(slug=slug_type)
        data = car.objects.filter(car_brand=br)
    types = brand.objects.all()
    return render(request, 'base.html', {'data': data,'type': types})
