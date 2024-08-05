from AppTade import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('profesor/',views.profesor, name="profesor"),
    path('cursos',views.cursos, name="cursos"),
]