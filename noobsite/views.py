from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def just_view(request):
    return HttpResponse("É so isto mesmo.")

def nothing_view(request):
    return HttpResponse("Não há mais nada!")

def smile_view(request):
    return HttpResponse(":)")
