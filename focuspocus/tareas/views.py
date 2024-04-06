from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView, CreateView
from tareas.models import Tarea


"""
    Todooms:
        - Hacer login - Como hacer un login Django.
        - Pedir Login en las vistas pertinentes
        - Agregar llave foranea al modelo Tarea ( para el usuario )
        - Al crear el objeto tarea asignar al usuario que lo esta haciendo ( CrearTarea Post -> Request.user )
        - En ListarTareas Filtrar por usuario ( ListarTareas Get -> Tarea.objects.filter(variable=request.user) <-- Retornarlo al template mediante context[''] )
        - Hacer Logout
"""

# Create your views here.

class Prueba(TemplateView):
    template_name = 'index.html'


class ListarTareas(ListView):
    template_name = 'lista-tareas.html'
    model = Tarea

class CrearTarea(CreateView):
    template_name = 'crear_tarea.html'
    model = Tarea
    success_url = '/lista/'
    fields = ('__all__')

class ModificarTarea(UpdateView):
    template_name = 'crear_tarea.html'
    model = Tarea
    success_url = '/lista/'
    fields = ('__all__')

class EliminarTarea(DeleteView):
    template_name = 'eliminar_tarea.html'
    model = Tarea
    success_url = '/lista/'
    fields = ('__all__')