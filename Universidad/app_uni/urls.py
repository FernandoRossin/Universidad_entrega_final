from re import template
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", views.inicio, name="inicio"),
    path("carga_curso", views.carga_curso, name="carga_curso"),
    path("carga_estudiante", views.carga_estudiante, name="carga_estudiante"),
    path("carga_profesor", views.carga_profesor, name="carga_profesor"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar, name="buscar"),
    path("eliminar_curso/<int:id_curso>", views.eliminar_curso, name="eliminar_curso"),
    path("eliminar_estudiante/<int:id_estudiante>", views.eliminar_estudiante, name="eliminar_estudiante"),
    path("eliminar_profesor/<int:id_profesor>", views.eliminar_profesor, name="eliminar_profesor"),
    path("editar_curso/<int:id_curso>", views.editar_curso, name= "editar_curso"),
    path("editar_estudiante/<int:id_estudiante>", views.editar_estudiante, name= "editar_estudiante"),
    path("editar_profesor/<int:id_profesor>", views.editar_profesor, name= "editar_profesor"),
    path("login", views.login_request, name = 'Login'),
    path("registro", views.registro , name='Registro'),
    path("logout", LogoutView.as_view(template_name= "logout.html"), name= "Logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
    path("estudiantes",views.estudiantes,name="estudiantes"),
    path("profesores",views.profesores ,name="profesores"),
    path("cursos",views.cursos,name="cursos"),
    path("about",views.about,name="about")

]




