from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_uni.models import *
from django.template import loader
from app_uni.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    
    return render(request, "inicio.html")

def about(request):
    
    return render(request, "about.html")


def carga_estudiante(request):
    
    if request.method == "POST":
        
        mi_formulario = Estudiante_formulario(request.POST)
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre = datos['nombre'], apellido = datos['apellido'], email = datos['email'] )
            estudiante.save()
            return redirect('estudiantes')


    return render(request, "carga_estudiante.html")

def carga_profesor(request):
    
    if request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre = datos['nombre'], apellido = datos['apellido'], email = datos['email'], profesion = datos['profesion'])
            profesor.save()
            return redirect('profesores')

    return render(request, "carga_profesor.html")
 
def carga_curso(request):

    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre = datos['nombre'], camada = datos['camada'])
            curso.save()
            return redirect('cursos')


    return render(request, "carga_curso.html")
    
def buscar_curso(request):

    return render(request,"buscar_curso.html")


def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse('Campo vacio')


def estudiantes(request):
    
    estudiantes = Estudiante.objects.all()
        
    diccionario = {
        "estudiantes": estudiantes
         }
    '''
    datos_est = loader.get_template("estudiantes.html")
    datos = datos_est.render(diccionario)
    
    return HttpResponse(datos)
    '''
    return render(request,"estudiantes.html",diccionario)

def profesores(request):
    
    profesores = Profesor.objects.all()
    
    
    diccionario = {
        "profesores" : profesores       
         }
    
    return render(request,"profesores.html",diccionario)

def cursos(request):
    
    cursos = Curso.objects.all()
    
    diccionario = {
        "cursos": cursos }

    return render(request,"cursos.html",diccionario)


def eliminar_curso(request,id_curso):

    curso = Curso.objects.get(id=id_curso)
    curso.delete()

    return redirect('cursos')


def eliminar_estudiante(request,id_estudiante):

    estudiante = Estudiante.objects.get(id=id_estudiante)
    estudiante.delete()

    return redirect('estudiantes')

def eliminar_profesor(request,id_profesor):

    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()

    return redirect('profesores')


def editar_curso(request,id_curso):

    curso = Curso.objects.get(id = id_curso)
    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

        return redirect('cursos')
    else:
        mi_formulario = Curso_formulario()

    return render(request,"editar_curso.html", {"mi_formulario": mi_formulario,"curso":curso})

def editar_estudiante(request,id_estudiante):

    estudiante = Estudiante.objects.get(id = id_estudiante)
    if request.method == "POST":

        mi_formulario = Estudiante_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            estudiante.nombre = datos['nombre']
            estudiante.apellido = datos['apellido']
            estudiante.email = datos['email']
            estudiante.save()

        return redirect('estudiantes')
    else:
        mi_formulario = Estudiante_formulario()

    return render(request,"editar_estudiante.html", {"mi_formulario": mi_formulario,"estudiante":estudiante})

def editar_profesor(request,id_profesor):

    profesor = Profesor.objects.get(id = id_profesor)
    if request.method == "POST":

        mi_formulario = Profesor_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos['nombre']
            profesor.apellido = datos['apellido']
            profesor.email = datos['email']
            profesor.profesion = datos['profesion']
            profesor.save()

        return redirect('profesores')
    else:
        mi_formulario = Profesor_formulario()

    return render(request,"editar_profesor.html", {"mi_formulario": mi_formulario,"profesor":profesor})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password=contra)

            if user is not None:
                login(request,user)
                
                return render(request, "inicio.html")
                            
            else:
                return HttpResponse(f"Usuario incorrecto")
        else:
            #return HttpResponse(f"Form incorrecto {form}")  
            return render(request, "login_incorrecto.html", {"form":form})

    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def registro(request):

    if request.method == "POST":

        #form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST) 
        
        if form.is_valid():

            form.save()
            #return HttpResponse("Usuario creado")
            return render(request,"usuario_creado.html")
            
    else:
        #form = UserCreationForm()
        form = CustomUserCreationForm()
    
    return render(request, "registro.html", {"form":form})


def editar_perfil(request):

    usuario = request.user

    if request.method =="POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request,"inicio.html")
            

    else:
        miFormulario = UserEditForm(initial = {'email': usuario.email})
    
    return render(request,"editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


    










