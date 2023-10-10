from django.contrib import admin
from .models import Usuario,Tarea,Proyecto,Etiqueta,AsignacionTarea,Comentario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(AsignacionTarea)
admin.site.register(Comentario)