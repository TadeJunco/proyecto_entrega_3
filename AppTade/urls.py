from django.urls import path
from AppTade import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('profesor/', views.profesores, name="Profesor"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entregables/', views.entregables, name="Entregables"),
    path('form-comun/', views.form_comun, name="Form-Comun"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
]




