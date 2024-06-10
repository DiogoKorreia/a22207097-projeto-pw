from django.shortcuts import render

# Create your views here.

def latim_view(request):
    return render(request,"novaapp/latim.html")

def maislatim_view(request):
    return render(request,"novaapp/maislatim.html")

def aindamaislatim_view(request):
    return render(request,"novaapp/aindamaislatim.html")