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
    
    # selecionar sprints
    path('sprints_select/', views.sprint_select),
    path('sprint_dashboard/<str:instancia_sprint>', views.sprint_dashboard),
    path('sprint_add/', views.sprint_add),
    
    path('daily_dashboard/<str:instancia_daily>', views.daily_dashboard),
    
    path('sprint_backlog/<str:instancia_sprint>', views.ver_sprint_backlog),
    
    path('ver_backlog_produto/', views.ver_backlog_produto), 
    
    path('decision_select/', views.decision_select),
    path('decision_dashboard/<str:instancia_decisao>', views.decision_dashboard),
    
]