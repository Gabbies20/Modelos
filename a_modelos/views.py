from django.shortcuts import render
from .models import Proyecto, Tarea

# Create your views here.
def index(request):
    return render(request,'tareas/index.html',{})


#Crea una URL que muestre una lista de todos los proyectos de la aplicación con sus datos correspondientes.
def lista_proyectos(request):
    #Es conveniente utilizar select_related y prefech_related para que solamente acceda a la base de datos una vez.
    proyectos = Proyecto.objects.select_related("usuario_creador").prefetch_related('usuario,tareas')
    proyectos = Proyecto.objects.all()
    return render(request, 'tareas/lista_proyectos.html',{'proyectos_mostrar':proyectos})






#Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
def tareas_a_proyectos(request,id_proyecto):
    tareas = Tarea.filter(proyecto=id_proyecto).order_by('-fecha_de_creacion').all()
    return render (request,'tareas/tareas_asociadas.html',{'tareas_asociadas':tareas})
    