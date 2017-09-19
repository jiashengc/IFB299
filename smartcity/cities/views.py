from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from splash import models
import json

def cities(request):
    cities = models.City.objects.all()
    return render(request, 'cities/cities.html', context={
        "cities": serializers.serialize('json', cities),
    })

def city(request, cityName):
    foundCity = [1]
    foundCity[0] = models.City.objects.get(name=cityName)

    return render(request, 'cities/city.html', context = {
        "city": serializers.serialize('json', foundCity),
    })
