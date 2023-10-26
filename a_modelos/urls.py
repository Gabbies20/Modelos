from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('proyectos/listar', views.lista_proyectos,name='lista_proyectos'),
    path('tareas/listar/<int:id_proyecto>/',views.tareas_a_proyectos,name='tareas_a_proyectos'),
    path('usuarios/listar/<int:tarea_id>',views.usuarios_a_tareas,
    name='usuarios_a_tareas'),
    path('observaciones/listar/<str:texto>',views.tareas_t_concreto, name='tareas_t_concreto')
]
