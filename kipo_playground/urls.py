from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('instancias_teste/', views.instancias_teste),
    path('instancias_tipo/', views.instancias_tipo),
    path('instancias_tipo_show/', views.instancias_tipo_show)
]