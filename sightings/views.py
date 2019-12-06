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

def edit_squirrel(request, unique_squirrel_id):
    squirrel_obj = squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)

    if request.method == 'POST':
        form = squirrelform(request.POST, instance=squirrel_obj)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = squirrelform(instance=squirrel_obj)
    context = {
            'form': form
            }
    return render(request, 'sightings/edit.html', context)
