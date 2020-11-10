from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader

#from base_SCIA.models.administrador import Administrador
#from base_SCIA.models.clase import Clase
#from base_SCIA.models.datos_personales_docente import Datos_Personales_Docente
#from base_SCIA.models.disciplinas import Disciplinas
#from base_SCIA.models.disciplinas_cursadas import Disciplinas_Cursadas
#from base_SCIA.models.disciplinas_cursando import Disciplinas_Cursando
#from base_SCIA.models.disciplinas_por_cursar import Disciplinas_Por_Cursar
#from base_SCIA.models.docente import Docente
#from base_SCIA.models.estudiante import Estudiante
#from base_SCIA.models.login import Login
from base_SCIA.models.datos_personales import Datos_Personales
from base_SCIA.models.datos_procedencia import Datos_Procedencia

#from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView

from base_SCIA.forms import EstudianteModelForm
#from base_SCIA.forms import DocentesModelForm
#from django.shortcuts import redirect


#def estudiante_new(request):
#	form = EstudianteModelForm()
#	return render(request, 'succes.html', {'form': form})

#class EstudianteCreateView(CreateView):
#	template_name = 'AltaEstudiante.html'
#	form_class = EstudianteModelForm


#	def form_valid(self, form):
#		datos_personales = form['Datos_Personales'].save()
#		datos_procedencia = form['Datos_Procedencia'].save(commit=False)
#		datos_procedencia.datos_personales = datos_personales
#		datos_procedencia.save()

#		return HttpResponseRedirect(reverse('succes'))


#class SuccessView(TemplateView):
#	template_name = 'succes.html'

#class DocenteCreateView(CreateView):
#	template_name = 'AltaDocente.html'
#	form_class = DocentesModelForm


#	def form_valid(self, form):
#		datos_personales_docente = form['Datos_Personales_Docente'].save()
#		docente = form['Docente'].save(commit=False)
#		docente.datos_personales_docente= datos_personales_docente
#		docente.save()

#		return HttpResponseRedirect(reverse('succes'))
#
#class SuccessView(TemplateView):
#	template_name = 'succes.html'



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

#def AltaEstudiante (request):
#	return render(request,'AltaEstudiante.html'		)

def ListaDetalleEstudiante (request):
	lista = Datos_Personales.objects.filter()
	lista2 = Datos_Procedencia.objects.filter()
	lista3 = Tutor.objects.filter()
	return render(request,'ListaDetalleEstudiante.html',{
		'lista':lista,
		'lista2':lista2,
		'lista3':lista3,
		},
		)

def DatosPersonalesEstudiante (request):
	return render(request,'DatosPersonalesEstudiante.html')

def DatosAcademicosEstudiante (request):
	return render(request,'DatosAcademicosEstudiante.html')

def DatosProcedenciaEstudiante (request):
	return render(request,'DatosProcedenciaEstudiante.html')

#def AltaDocente (request):
#	return render(request,'AltaDocente.html')

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

def formulario (request):
	return render(request,'formulario.html')


#generacion de clases o vistas genericas

class EstudianteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaEstudiante.html"
	#model = Datos_Personales
	form_class = EstudianteModelForm
	#fields = ('__all__')
	success_url = 'ListaDetalleEstudiante.html'

#class DatosProcedenciaCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
#	template_name="AltaEstudiante.html"
#	model = Datos_Procedencia
#	fields = ('__all__')
#	success_url = '.'

#class TutorCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
#	template_name="AltaEstudiante.html"
#	model = Tutor
#	fields = ('__all__')
#	success_url = '.'


