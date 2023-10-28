from django.shortcuts import render
from .models import Proyecto, Tarea,AsignacionTarea,Comentario,Etiqueta,Usuario

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

  
  
  
  
  
  
  
  
    
# 6. Crear una URL que muestre todos las tareas que se han creado entre dos años y el estado sea “Completada”.
def tareas_years(request,year_inicio,year_fin):
    #No lo pasamos por parametro y asignamos directamente el valor:
    #ano_inicio = 2000
    #ano_fin = 2005
    tarea = Tarea.objects.all()
    tarea = tarea.filter(estados='COM').filter(fecha_de_creacion__year__range=[year_inicio, year_fin])
    #El filtro con una sola línea y usando los operadores gt y lt:
    #tareas_entre_anos = Tarea.objects.filter(estados='COM', fecha_de_creacion__year__gt=ano_inicio, fecha_de_creacion__year__lt=ano_fin)
    return render(request,'tareas/tareas_years.html',{'tareas_years':tarea})







# 7. Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.
def ultimo_usuario(request, id_proyecto):
    comentario = Comentario.objects.select_related('usuario','tarea').all()
    comentario = comentario.order_by('-fecha_de_contenido').filter(tarea__proyecto= id_proyecto)
    #__ Con estos doble guiones accedo a un campo de mi modelo tarea.
    
    return render(request,'tareas/comentario_ultimo_usuario.html',{'comentario_mostrar':comentario})
    
    
# 8. Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.
def comentarios_palabra_year(request,id_tarea,palabra,year):
    tarea = Tarea.objects.get(id=id_tarea)
    comentario = Comentario.objects.select_related('usuario','tarea').filter(contenido__contains=palabra,tarea=id_tarea,fecha_de_contenido__year=year)
    
    #En mi plantilla quiero mostrar los parametros que envio en la url, por lo que voy a crear un diccionario que lo contenga:
    contexto = {
        'comentario_mostrar':comentario,
        'palabra':palabra,
        'year': year
    }
    return render(request,'tareas/comentario_palabra_year.html',contexto)

    
# 9. Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas de un proyecto.
    
def etiquetas_en_tarea(request):
    #etiqueta = Etiqueta.objects.prefetch_related('tarea')
    etiqueta = Etiqueta.objects.all()
    return render(request, 'tareas/etiquetas_tarea.html',{'etiqueta_mostrar':etiqueta})


# 10. Crear una URL que muestre todos los usuarios que no están asignados a una tarea.
def usuarios_no_asignados(request):
    usuarios_no_asignados = Usuario.objects.exclude(tarea__usuarios_asignados__isnull=False)
    return render(request, 'tareas/usuarios_no_asignados.html', {'usuarios_no_asignados': usuarios_no_asignados})
    
    
    
    
    
    
    
    
    
    
    
    




    