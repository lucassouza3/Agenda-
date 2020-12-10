from django.db import models
from django.contrib.auth.models import User
from time import strftime
# Create your models here.

class Evento(models.Model): #Entidade Evento // Tabela Evento
    titulo = models.CharField(max_length=100,verbose_name='Título') #Atributo título
    descricao = models.TextField(blank=True, null=True) #Atributo Descrição
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #Atributo data do evento
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data da Criação") #atributo data da criação
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Evento'
    def __str__(self):
        return self.titulo
    def get_data_evento(self):
        return self.data_evento.strftime('criado em: %d/%m/%Y às %H:%M')