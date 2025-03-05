from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def portao(request):
    return HttpResponse('Você chegou ao portão da casa')

def sala(request):
    return HttpResponse('Você chegou à sala da casa, sente-se no sofá')

def quarto(request):
    return HttpResponse('Você chegou ao quarto da casa, vá dormir')

def post_list(request):
    return render(request, 'blog/post_list.html', {}) # O template é blog/post_list.html que está na pasta templates/blog e o contexto é um dicionário vazio {}.
