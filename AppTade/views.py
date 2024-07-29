from django.shortcuts import render
from .models import Curso
from AppTade.forms import CursoFormulario, BuscaCursoForm


def inicio(request):
    return render(request, "App1/index.html")

def profesor(request):
    return render(request, "App1/profesor.html")

def cursos(request):
    return render(request, "App1/cursos.html")

def estudiantes(request):
    return render(request, "App1/estudiantes.html")

def entregables(request):
    return render(request, "App1/entregables.html")


def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "App1/index.html")

    return render(request,"App1/curso_formulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()

            return render(request, "App1/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "App1/form_con_api.html", {"mi_formulario": mi_formulario})


def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "App1/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "App1/buscar_form_con_api.html", {"mi_formulario": mi_formulario})


