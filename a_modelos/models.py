from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=50,unique=True)
    contraseña = models.CharField(max_length=20)
    fecha_de_registro = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.nombre    
    
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_de_inicio = models.DateField()
    fecha_de_finalizacion = models.DateField()
    usuario = models.ManyToManyField(Usuario,
                                     related_name='usuario')
    usuario_creador = models.ForeignKey(Usuario,
                                        on_delete=models.CASCADE,
                                        related_name="usuario_creador")

    def __str__(self) -> str:
        return self.nombre
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    ESTADOS=[
        ('PEN','Pendiente'),
        ('PRO','Progreso'),
        ('COM','Completada'),
    ]
    estados = models.CharField(
                                max_length=3,
                                choices=ESTADOS,
                                default='PEN',
    )
    completada = models.BooleanField(default=False)
    fecha_de_creacion = models.DateField()
    hora_de_vencimiento = models.TimeField()
    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuarios_asignados = models.ManyToManyField(Usuario,
                                                through='AsignacionTarea',
                                                related_name="usuarios_asignados")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
       
       
    def __str__(self) -> str:
        return self.titulo

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    tarea = models.ManyToManyField(Tarea)
    
    def __str__(self) -> str:
        return self.nombre
    
class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    observaciones = models.TextField()
    fecha_de_asignacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.observaciones

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_de_contenido = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    
    
    
    

    