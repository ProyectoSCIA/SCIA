from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import TemplateView
from base_SCIA.models.datos_aspirantes import Datos_Aspirantes
from base_SCIA.models.datos_procedencia import Datos_Procedencia
from base_SCIA.models.tutor import Tutor
from base_SCIA.models.estudiante import Estudiante
from base_SCIA.models.administrador import Administrador

#agregar estudiante
from base_SCIA.forms import EstudianteModelForm


#agregar aspirantes
class DatosAspirantesCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAspirante.html"
	model = Datos_Aspirantes
	fields = ('__all__')
	success_url = 'Menu'

#Menu
class Menu1(TemplateView):
	template_name = 'Menu.html'


#alta estudiante
class EstudianteCreateView(CreateView):
	template_name = 'AltaDatos.html'
	form_class = EstudianteModelForm

	def form_valid(self, form):
		datos_procedencia = form['Datos_Procedencia'].save()
		tutor = form['Tutor'].save(commit=False)
		tutor = tutor
		tutor.save()
		return HttpResponseRedirect('AltaEstudiante')

class Guardar2(TemplateView):
	template_name = 'AltaEstudiante.html'

#datos estudiante
class AltaEstudianteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaEstudiante.html"
	model = Estudiante
	fields = ('__all__')
	success_url = 'succes'

class Guardar3(TemplateView):
	template_name = 'succes.html'

#Alta admnistrador
class AdministradorCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAdministrador.html"
	model = Administrador
	fields = ('__all__')
	success_url = 'succes'

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
