from django.shortcuts import render, redirect

from typedocuments.models import Typedocument

def typedocuments(request):    
    typedocuments_list = Typedocument.objects.all()    
    return render(request, 'typedocuments/index.html', {'typedocuments_list': typedocuments_list})

def change_status_typedocument(request, typedocument_id):
    typedocument = Typedocument.objects.get(pk=typedocument_id)
    typedocument.status = not typedocument.status
    typedocument.save()
    return redirect('typedocuments')