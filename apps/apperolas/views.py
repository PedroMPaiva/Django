from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Frase

# Create your views here.
def home(request):
    frase = Frase.objects.all()
    return render(request, 'index.html', {'frase': frase})



def home(request):
    if request.method == 'POST':
        nova_frase = request.POST.get('nova_frase')
        autor = request.POST.get('autor')
        Frase.objects.create(texto=nova_frase, autor=autor, user=request.user)
    frase = Frase.objects.all()
    return render(request, 'index.html', {'frase': frase})
