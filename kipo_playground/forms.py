"""Módulo de Forms de kipo_playground

"""

from django.forms import ModelForm
from django import forms

from .models import novo_instancias_tipo, inserir_instancias_tipo, inserir_instancias_sprint

class inserir_instancias_tipoForm(ModelForm):
    
    class Meta:
        model = inserir_instancias_tipo
        fields = ['nome', 'classe', 'observacao']
        

class novo_instancias_tipoForm(ModelForm):
    
    class Meta:
        model = novo_instancias_tipo
        fields = ['busca']
        
class inserir_instancias_sprintForm(ModelForm):
    
    class Meta:
        model = inserir_instancias_sprint
        fields = ['nome', 'observacao']
        