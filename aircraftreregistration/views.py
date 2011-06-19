from django.shortcuts import render_to_response, get_object_or_404
from faadata.aircraft.models import *

def find_dates(request, n_number):
    if n_number[0] == 'N' or n_number[0] == 'n':
        n_number = n_number[1:] # strip off the beginning, the FAA doesn't store with a leading N
    aircraft = get_object_or_404(AircraftRegistration, n_number__iexact=n_number)

    return render_to_response('dates.html', {'aircraft': aircraft,})

def index(request):
    return render_to_response('index.html', {'url': 'http://rereg.wxgk.net'})

def tech(request):
    return render_to_response('tech.html', {})
