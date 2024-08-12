from django.shortcuts import render
from .models import Curso
from AppTade.forms import CursoFormulario, BuscaCursoForm

def inicio(request):
    return render(request, "App1/index.html")

def cursos(request):
    return render(request, "App1/cursos.html")

def profesores(request):
    return render(request, "App1/profesores.html")

def estudiantes(request):
    return render(request, "App1/estudiantes.html")

def entregables(request):
    return render(request, "App1/entregables.html")

def form_comun(request):

    if request.method == 'POST':

        curso =  Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "App1/index.html")

    return render(request,"App1/form_comun.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "App1/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "App1/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "App1/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "App1/buscar_form_con_api.html", {"miFormulario": miFormulario})


