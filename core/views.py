from projeto_lucas.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import redirect, render
from django.http import HttpResponse, request, HttpRequest
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

#ListaEventos
@login_required(login_url='/login/')
def listaEventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario,
    data_evento__gt=data_atual)
    dados = {'evento':evento}
    return render(request,'agenda.html', dados)

#Logar
def login_user(request):
    return render(request, 'login.html')

#Deslogar
def logout_user(request):
    logout(request)
    return redirect('/')

#Salvar login
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return redirect('/')

#Evento
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento']= Evento.objects.get(id=id_evento)
    return render(request, 'evento.html')

#Salvar Evento
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local_evento = request.POST.get('local_evento')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.local_evento = local_evento
                evento.save()
            '''Evento.objects.filter(id=id_evento).update(titulo='titulo',
             data_evento='data_evento',
              descricao='descricao',
               local_evento='local_evento',)'''
        else:
            Evento.objects.create(titulo='titulo',
             data_evento='data_evento',
              descricao='descricao',
               local_evento='local_evento',
                usuario=request.user,)
        return redirect('/')

#Deletar
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


#JsonListaEvenos
@login_required(login_url='/login/')
def json_lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id','titulo')
    dados = {'evento':evento}
    return JsonResponse(list(evento),safe=False)

