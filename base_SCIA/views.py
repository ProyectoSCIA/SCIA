from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
from base_SCIA.models.administrador import Administrador
from base_SCIA.models.clase import Clase
from base_SCIA.models.datos_academicos import Datos_Academicos
from base_SCIA.models.datos_docente import Datos_Docente
from base_SCIA.models.datos_personales import Datos_Personales
from base_SCIA.models.datos_personales_docente import Datos_Personales_Docente
from base_SCIA.models.datos_procedencia import Datos_Procedencia
from base_SCIA.models.disciplinas import Disciplinas
from base_SCIA.models.disciplinas_cursadas import Disciplinas_Cursadas
from base_SCIA.models.disciplinas_cursando import Disciplinas_Cursando
from base_SCIA.models.disciplinas_por_cursar import Disciplinas_Por_Cursar
from base_SCIA.models.docente import Docente
from base_SCIA.models.estudiante import Estudiante
from base_SCIA.models.login import Login
from base_SCIA.models.tutor import Tutor


def encabezado (request):
	return render(request,'encabezado.html')

def footer (request):
	return render(request,'footer.html')

def home (request):
	return render(request,'home.html')

def login (request):
	return render(request,'login.html')

def encabezado2 (request):
	return render(request,'encabezado2.html')

def encabezadoE (request):
	return render(request,'encabezadoE.html')

def AltaEstudiante (request):
	return render(request,'AltaEstudiante.html')

def ListaDetalleEstudiante (request):
	return render(request,'ListaDetalleEstudiante.html')

def DatosPersonalesEstudiante (request):
	return render(request,'DatosPersonalesEstudiante.html')

def DatosAcademicosEstudiante (request):
	return render(request,'DatosAcademicosEstudiante.html')

def DatosProcedenciaEstudiante (request):
	return render(request,'DatosProcedenciaEstudiante.html')

def AltaDocente (request):
	return render(request,'AltaDocente.html')

def ListaDetalleDocente (request):
	return render(request,'ListaDetalleDocente.html')

def DatosPersonalesDocente (request):
	return render(request,'DatosPersonalesDocente.html')

def DatosAcademicosDocente (request):
	return render(request,'DatosAcademicosDocente.html')

def PublicarAvisos (request):
	return render(request,'PublicarAvisos.html')

def lateral (request):
	return render(request,'lateral.html')
