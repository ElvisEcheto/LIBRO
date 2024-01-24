from django.shortcuts import render, redirect

from typelodgings.models import Typelodging

def typelodgings(request):    
    typelodgings_list = Typelodging.objects.all()    
    return render(request, 'typelodgings/index.html', {'typelodgings_list': typelodgings_list})

def change_status_typelodging(request, typelodging_id):
    typelodging = Typelodging.objects.get(pk=typelodging_id)
    typelodging.status = not typelodging.status
    typelodging.save()
    return redirect('typelodgings')