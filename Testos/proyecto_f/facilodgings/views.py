from django.shortcuts import render, redirect

from facilodgings.models import Facilodgings

def facilodgings(request):    
    facilodgings_list = Facilodgings.objects.all()    
    return render(request, 'facilodgings/index.html', {'facilodgings_list': facilodgings_list})

def change_status_facilodging(request, facilodging_id):
    facilodging = Facilodgings.objects.get(pk=facilodging_id)
    facilodging.status = not facilodging.status
    facilodging.save()
    return redirect('facilodgings')