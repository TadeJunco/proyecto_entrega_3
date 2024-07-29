from AppTade import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('profesor/',views.profesor, name="profesor"),
    path('cursos',views.cursos, name="cursos"),
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]