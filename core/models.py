from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from time import strftime
# Create your models here.

class Evento(models.Model): #Entidade Evento // Tabela Evento
    titulo = models.CharField(max_length=100,verbose_name='Título') #Atributo título
    local_evento = models.CharField(max_length=100, verbose_name='Local', null=True, blank=True) #Atributo local
    descricao = models.TextField(blank=True, null=True) #Atributo Descrição
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #Atributo data do evento
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data da Criação") #atributo data da criação
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'evento'
    
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('criado em: %d/%m/%Y às %H:%M')
    
    def get_input_data_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
        
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False