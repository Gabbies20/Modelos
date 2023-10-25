from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('proyectos/listar', views.lista_proyectos,name='lista_proyectos'),
    path('tareas/listar',views.tareas_a_proyectos,name='tareas_a_proyectos')
]
