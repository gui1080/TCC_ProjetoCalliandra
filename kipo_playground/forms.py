"""Módulo de Forms de kipo_playground

Em base de modelos estabelecidos, contém formulários para inserir uma nova instância, para recuperar as instâncias de um tipo e para inserir uma sprint nova.

"""

from django.forms import ModelForm
from django import forms

from .models import MateriaJornalistica, novo_instancias_tipo, inserir_instancias_tipo, inserir_instancias_dada_classe, definir_obs_backlogitem, definir_status_backlogitem, definir_esforco_backlogitem


class MateriaJornalistica_Form(ModelForm):
    
    class Meta:
        model = MateriaJornalistica
        fields = ['id', 'titulo', 'texto', 'sutien', 'editores', 'autores', 'main_keyword']


class definir_esforco_backlogitem_Form(ModelForm):
    
    class Meta:
        model = definir_esforco_backlogitem
        fields = ['esforco']

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
        

class definir_status_backlogitem_Form(ModelForm):

    class Meta:
        model = definir_status_backlogitem
        fields = ['classe']
        

class definir_obs_backlogitem_Form(ModelForm):
    
    class Meta:
        model = definir_obs_backlogitem
        fields = ['observacao']
        