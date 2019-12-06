from django.shortcuts import render
from .models import squirrel
from django.http import HttpResponse

def index(request):
    squirrel_list = list(squirrel.objects.all())
    context = {'squirrel_list': squirrel_list}
    return render(request, 'sightings/index.html', context)
