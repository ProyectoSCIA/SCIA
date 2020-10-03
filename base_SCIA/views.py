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