from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models import Evento
'''
def index(request):
    return redirect('/agenda/')
'''
def listaEventos(request):
    evento = Evento.objects.get(id=1)
    dados = {'evento':evento}
    return render(request,'agenda.html', dados)