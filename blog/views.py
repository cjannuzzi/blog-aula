from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {}) # O template é blog/post_list.html que está na pasta templates/blog e o contexto é um dicionário vazio {}.

def portao(request):
    return render(request,'blog/porta.html', {}) 

def sala(request):
    return render(request,'blog/sala-simples.html', {}) 

def quarto(request):
    return render(request,'blog/quarto-simples.html', {})


