from django.shortcuts import render
from .models import Proyecto, Tarea,AsignacionTarea

# 1. Create your views here.
def index(request):
    proyecto = Proyecto.objects.all()
    return render(request,'tareas/index.html',{'proyecto_id': proyecto})


#2. Crea una URL que muestre una lista de todos los proyectos de la aplicación con sus datos correspondientes.
def lista_proyectos(request):
    #Es conveniente utilizar select_related y prefech_related para que solamente acceda a la base de datos una vez.
    proyectos = Proyecto.objects.select_related("usuario_creador").prefetch_related('usuario').all()
    return render(request, 'tareas/lista_proyectos.html',{'proyectos_mostrar':proyectos})




#3. Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
def tareas_a_proyectos(request,id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tareas = Tarea.objects.select_related('usuario_creador','proyecto').prefetch_related('usuarios_asignados').filter(proyecto=proyecto).order_by('-fecha_de_creacion').all()
    return render (request,'tareas/tareas_asociadas.html',{'tareas_asociadas':tareas, 'proyecto':proyecto})



# 4. Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 
def usuarios_a_tareas(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    usuarios = AsignacionTarea.objects.filter(tarea=tarea).order_by('fecha_de_asignacion')
    return render (request,'tareas/usuarios_asignados.html',{'mostrar_usuarios':usuarios, 'tareas':tarea})
    
    
# 5. Crear una URL que muestre todas las tareas que tengan un texto en concreto en las observaciones a la hora de asignarlas a un usuario.
def tareas_t_concreto(request,texto):
    tarea = AsignacionTarea.objects.select_related('tarea','usuario')
    #La expresión observaciones__icontains=texto se utiliza para filtrar las tareas cuyo campo observaciones contiene (de manera insensible a mayúsculas y minúsculas) el texto especificado.
    #observaciones es el nombre del campo en el modelo de tarea que se está utilizando como base para el filtro. En este caso, se busca en el campo observaciones.
    #__icontains es un operador de consulta de Django que indica que deseas realizar una búsqueda que sea "insensible a mayúsculas y minúsculas". Esto significa que la consulta buscará todas las tareas cuyo campo observaciones contenga el valor de texto sin importar si las letras son mayúsculas o minúsculas.
    #texto es el valor con el que deseas comparar el campo observaciones. En otras palabras, se están buscando todas las tareas cuyas observaciones contengan el texto especificado en texto.
    #
    tarea = tarea.filter(observaciones__icontains=texto)
    return render(request,'tareas/tareas_texto.html',{'tareas_con_texto':tarea})

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




    