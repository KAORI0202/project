from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count

from .models import Squirrel
from .forms import SquirrelForm

def sightings(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'tracker/sightings.html', context)

def update(request, unique_squirrel_ID):
    squirrel = get_object_or_404(Squirrel, pk = unique_squirrel_ID)
    if request.method == 'POST':
        # check data with form
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/tracker/sightings/{unique_squirrel_ID}')
    else:
        # build empty form
        form = SquirrelForm(instance = squirrel)
    context = {
        'form': form,
    }
    return render(request, 'tracker/update.html', context)

def create(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/tracker/sightings/{unique_squirrel_ID}')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'tracker/create.html', context)

def stats(request):
    total_sightings = Squirrel.objects.count()
    shift_stats = Squirrel.objects.values('shift').annotate(shift_count = Count('shift')).order_by('shift')
    age_stats = Squirrel.objects.values('age').annotate(age_count = Count('age')).order_by('age')
    primary_fur_color_stats = Squirrel.objects.values('primary_fur_color').annotate(primary_fur_color_count = Count('primary_fur_color')).order_by('primary_fur_color')
    location_stats = Squirrel.objects.values('location').annotate(location_count = Count('location')).order_by('location')

    context = {
        'total_sightings': total_sightings,
        'shift_stats': shift_stats,
        'age_stats': age_stats,
        'primary_fur_color_stats': primary_fur_color_stats,
        'location_stats': location_stats,
    }
    return render(request, 'tracker/stats.html', context)

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
        'sightings': sightings,
    }
    return render(request, 'tracker/map.html', context)
# Create your views here.
