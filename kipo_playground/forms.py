from django.forms import ModelForm
from django import forms

from .models import novo_instancias_tipo

class novo_instancias_tipoForm(ModelForm):
    
    class Meta:
        model = novo_instancias_tipo
        fields = ['busca']