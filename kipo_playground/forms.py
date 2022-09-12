"""Módulo de Forms de kipo_playground

Em base de modelos estabelecidos, contém formulários para inserir uma nova instância, para recuperar as instâncias de um tipo e para inserir uma sprint nova.

"""

from django.forms import ModelForm
from django import forms

from .models import novo_instancias_tipo, inserir_instancias_tipo, inserir_instancias_dada_classe

class inserir_instancias_dada_classeForm(ModelForm):
    
    class Meta:
        model = inserir_instancias_dada_classe
        fields = ['nome', 'observacao']
    

class inserir_instancias_tipoForm(ModelForm):
    
    class Meta:
        model = inserir_instancias_tipo
        fields = ['nome', 'classe', 'observacao']
        

class novo_instancias_tipoForm(ModelForm):
    
    class Meta:
        model = novo_instancias_tipo
        fields = ['busca']
        
