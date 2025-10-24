from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
	cursos = Curso.objects.all()
	messages.success(request, '¡Cursos listados!')
	return render(request, "gestionCursos.html", {'cursos': cursos})

def registrarCurso(request):
	codigo=request.POST['codigo']
	nombre=request.POST['nombre']
	creditos=request.POST['creditos']

	curso=Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
	messages.success(request, '¡Curso registrado!')
	return redirect('/')

def editarCurso(request,codigo):
	curso = Curso.objects.get(codigo=codigo)
	return render(request, "editarCursos.html", {"curso": curso})

def editarCursoForm(request):
	codigo=request.POST['codigo']
	nombre=request.POST['nombre']
	creditos=request.POST['creditos']

	curso = Curso.objects.get(codigo=codigo)
	curso.nombre = nombre
	curso.creditos = creditos

	curso.save()
	messages.success(request, '¡Curso Actualizado!')
	return redirect('/')

def eliminarCurso(request,codigo):
	curso = Curso.objects.get(codigo=codigo)
	curso.delete()
	messages.success(request, '¡Curso Eliminado!')
	return redirect('/')

