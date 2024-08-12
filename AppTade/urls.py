from AppTade import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('profesor/',views.profesor, name="profesor"),
    path('cursos',views.cursos, name="cursos"),
    path('entregables/', views.entregables, name="Entregables"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
]

clase_21 = [
    path('form-comun/', views.curso_formulario, name="Form-Comun"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]

urlpatterns += clase_21