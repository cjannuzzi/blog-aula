from django.urls import path # Importa a função path
from . import views # Importa a view do app blog

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('portao', views.portao),
    path('sala', views.sala),
    path('quarto', views.quarto),
] 
