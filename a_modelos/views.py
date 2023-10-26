from django.shortcuts import render
from .models import Proyecto, Tarea,AsignacionTarea

# Create your views here.
def index(request):
    return render(request,'tareas/index.html',{})


#Crea una URL que muestre una lista de todos los proyectos de la aplicación con sus datos correspondientes.
def lista_proyectos(request):
    #Es conveniente utilizar select_related y prefech_related para que solamente acceda a la base de datos una vez.
    proyectos = Proyecto.objects.select_related("usuario_creador").prefetch_related('usuario').all()
    return render(request, 'tareas/lista_proyectos.html',{'proyectos_mostrar':proyectos})




#Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
def tareas_a_proyectos(request,id_proyecto):
    tareas = Tarea.objects.select_related('usuario_creador','proyecto').prefetch_related('usuarios_asignados')
    tareas = tareas.filter(proyecto=id_proyecto).order_by('-fecha_de_creacion').all()
    return render (request,'tareas/tareas_asociadas.html',{'tareas_asociadas':tareas})




#Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 
def usuarios_a_tareas(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    usuarios = AsignacionTarea.objects.filter(tarea=tarea).order_by('fecha_de_asignacion')
    return render (request,'tareas/usuarios_asignados.html',{'mostrar_usuarios':usuarios})
    
    
#Crear una URL que muestre todas las tareas que tengan un texto en concreto en las observaciones a la hora de asignarlas a un usuario.
def tareas_t_concreto(request,texto):
    tarea = AsignacionTarea.objects.select_related('tarea','usuario')
    tarea = tarea.filter(observaciones__icontains=texto)
    return render(request,'tareas/tareas_texto.html',{'tareas_con_texto':tarea})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




    