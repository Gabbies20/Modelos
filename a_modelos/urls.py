from django.urls import path
from .import views
from django.views.defaults import page_not_found



urlpatterns = [
    path('', views.index,name='index'),
    path('proyectos/listar', views.lista_proyectos,name='lista_proyectos'),
    path('tareas/<int:id_proyecto>/listar/',views.tareas_a_proyectos,name='tareas_a_proyectos'),
    path('usuarios/listar/<int:tarea_id>',views.usuarios_a_tareas,
    name='usuarios_a_tareas'),
    path('observaciones/listar/<str:texto>',views.tareas_t_concreto, name='tareas_t_concreto'),
    path('tareas-texto/<str:texto>',views.tareas_t_concreto,name='tareas_texto'),
    path('tareas-years/<int:year_inicio>/<int:year_fin>/',views.tareas_years,name='tareas_years'),
    path('comentario/<int:id_proyecto>/',views.ultimo_usuario,name='ultimo_usuario'),
    path('comentario-palabra/<int:id_tarea>/<str:palabra>/<int:year>/',views.comentarios_palabra_year,name='comentario_palabra'),
    path('etiquetas/',views.etiquetas_en_tarea,name='etiquetas'),
    path('usuarios-no-asignados/',views.usuarios_no_asignados,name='usuarios_no_asignados')
]
