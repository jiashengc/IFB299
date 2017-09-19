from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from splash import models
import json

# Create your views here.
def city(request):
    cities = models.City.objects.all()
    return render(request, 'city/city.html', context={
        "cities": serializers.serialize('json', cities),
    })
