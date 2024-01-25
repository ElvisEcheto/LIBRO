from django import forms
from . models import Costumer

from typedocuments.models import Typedocument

class CostumerForm(forms.ModelForm):
    Typedocument = forms.ModelChoiceField(queryset=Typedocument.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Costumer
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'document': 'documento',
            'typedocument': 'tipo documento',
            'phone': 'Numero',                  
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el código del libro'}),
            'document': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),   
            'phone': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio del libro'}),    
        }