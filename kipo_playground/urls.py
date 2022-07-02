from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('instancias_teste/', views.instancias_teste)
]