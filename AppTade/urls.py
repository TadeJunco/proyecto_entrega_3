from django.urls import path
from AppTade import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About")
]

# Cursos
urlpatterns += [
    path('curso-list/', views.CursoListView.as_view(), name="CursoList"),
    path('curso-detail/<int:pk>/', views.CursoDetailView.as_view(), name="CursoDetail"),
    path('curso-create/', views.CursoCreateView.as_view(), name="CursoCreate"),
    path('curso-update/<int:pk>/', views.CursoUpdateView.as_view(), name="CursoUpdate"),
    path('curso-delete/<int:pk>/', views.CursoDeleteView.as_view(), name="CursoDelete"),
]

# Estudiantes
urlpatterns += [
    path('estudiante-list/', views.EstudianteListView.as_view(), name="EstudianteList"),
    path('estudiante-detail/<int:pk>/', views.EstudianteDetailView.as_view(), name="EstudianteDetail"),
    path('estudiante-create/', views.EstudianteCreateView.as_view(), name="EstudianteCreate"),
    path('estudiante-update/<int:pk>/', views.EstudianteUpdateView.as_view(), name="EstudianteUpdate"),
    path('estudiante-delete/<int:pk>/', views.EstudianteDeleteView.as_view(), name="EstudianteDelete"),
]

# # Profesores
urlpatterns += [
    path('profesor-list/', views.ProfesorListView.as_view(), name="ProfesorList"),
    path('profesor-detail/<int:pk>/', views.ProfesorDetailView.as_view(), name="ProfesorDetail"),
    path('profesor-create/', views.ProfesorCreateView.as_view(), name="ProfesorCreate"),
    path('profesor-update/<int:pk>/', views.ProfesorUpdateView.as_view(), name="ProfesorUpdate"),
    path('profesor-delete/<int:pk>/', views.ProfesorDeleteView.as_view(), name="ProfesorDelete"),
]

# # Entregables
urlpatterns += [
    path('entregable-list/', views.EntregableListView.as_view(), name="EntregableList"),
    path('entregable-detail/<int:pk>/', views.EntregableDetailView.as_view(), name="EntregableDetail"),
    path('entregable-create/', views.EntregableCreateView.as_view(), name="EntregableCreate"),
    path('entregable-update/<int:pk>/', views.EntregableUpdateView.as_view(), name="EntregableUpdate"),
    path('entregable-delete/<int:pk>/', views.EntregableDeleteView.as_view(), name="EntregableDelete"),
]




