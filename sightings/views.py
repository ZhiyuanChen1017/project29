from django.shortcuts import render
from .models import squirrel
from django.http import HttpResponse

def map(request):
    squirrel_list = list(squirrel.objects.all())[:100]
    context = {'sightings': squirrel_list}
    return render(request, 'sightings/map.html', context)

def index(request):
    squirrel_list = list(squirrel.objects.all())
    context = {'squirrel_list': squirrel_list}
    return render(request, 'sightings/index.html', context)
