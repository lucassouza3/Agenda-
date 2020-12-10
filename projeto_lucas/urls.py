from django.contrib import admin
from django.urls import path
from core import views
from core.models import Evento
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.listaEventos),
    path('', RedirectView.as_view(url='agenda/')),
]