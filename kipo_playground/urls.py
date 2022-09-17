"""Módulo de URLs de kipo_playground

Define uma lista com as possíveis URLs e sua equivalências com as suas views.

"""

from django.urls import path
from . import views

urlpatterns = [
    
    # Tela de início
    path('welcome/', views.welcome),
    
    # Sobre
    path('sobre/', views.sobre), 
    
    # Teste para ver instâncias
    path('instancias_teste/', views.instancias_teste),
    
    # ver instâncias por tipo
    path('instancias_tipo/', views.instancias_tipo),
    path('instancias_tipo_show/', views.instancias_tipo_show), 
    
    # Inserir instâncias
    path('inserir_instancia/', views.inserir_instancia),
    path('inserir_instancia_tela_ok/', views.inserir_instancia_tela_ok),
    path('retirar_instancia/<str:instancia>', views.retirar_instancia),
    
    # selecionar sprints
    path('sprint_select/', views.sprint_select),
    path('sprint_dashboard/<str:instancia_sprint>', views.sprint_dashboard),
    path('add_classe/<str:classe_inst>', views.add_classe),
    path('add_classe_com_relacionamento/<str:classe_inst>/<str:relacinamento_inst>/<str:referencia_inst>', views.add_classe_com_relacionamento),
    path('sprint_options/<str:instancia_sprint>', views.sprint_options),
    
    # visualização de dashboard
    path('daily_dashboard/<str:instancia_daily>', views.daily_dashboard),
    path('sprint_backlog/<str:instancia_sprint>', views.ver_sprint_backlog),
    
    # backlog do produto
    path('ver_backlog_produto/', views.ver_backlog_produto), 
    
    # visualização da decisão
    path('decision_select/', views.decision_select),
    path('decision_dashboard/<str:instancia_decisao>', views.decision_dashboard),
    
]