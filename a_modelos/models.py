from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=50,unique=True)
    contraseña = models.CharField(max_length=20)
    fecha_de_registro = models.DateTimeField()
    
    
    
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
    

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_de_inicio = models.DateField()
    fecha_de_finalizacion = models.DateField()
    

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    
    
class AsignacionTarea(models.Model):
    observaciones = models.TextField()
    fecha_de_asignacion = models.DateTimeField()
    

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_de_contenido = models.DateTimeField()
    
    

    