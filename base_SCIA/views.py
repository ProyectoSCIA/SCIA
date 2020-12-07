from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import TemplateView, UpdateView
#from django.urls import reverse_lazy

from base_SCIA.models.datos_aspirantes import Datos_Aspirantes
from base_SCIA.models.datos_procedencia import Datos_Procedencia
from base_SCIA.models.tutor import Tutor
from base_SCIA.models.estudiante import Estudiante
from base_SCIA.models.administrador import Administrador
from base_SCIA.models.docente import Docente
from base_SCIA.models.disciplinas import Disciplinas
from base_SCIA.models.clase import Clase
from base_SCIA.models.disciplinas_cursando import Disciplinas_Cursando
from base_SCIA.models.disciplinas_cursadas import Disciplinas_Cursadas

#agregar estudiante
from base_SCIA.forms import EstudianteModelForm
#from base_SCIA.forms import AspiranteModelForm

#agregar aspirantes
class DatosAspirantesCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAspirante.html"
	model = Datos_Aspirantes
	fields = ('__all__')
	success_url = 'ListaDetalleAspirante'

#datos tutor,procedencia de estudiante
class DatosCreateView(CreateView):
	template_name = 'AltaDatos.html'
	form_class = EstudianteModelForm

	def form_valid(self, form):
		datos_procedencia = form['Datos_Procedencia'].save()
		tutor = form['Tutor'].save(commit=False)
		tutor.datos_procedencia = datos_procedencia
		tutor.save()
		return HttpResponseRedirect('Guardar2')

class Guardar2(TemplateView):
	template_name = 'AltaEstudiante.html'

#datos estudiante
class AltaEstudianteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaEstudiante.html"
	model = Estudiante
	fields = ('__all__')
	success_url = '.'

#Alta admnistrador
class AdministradorCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAdministrador.html"
	model = Administrador
	fields = ('__all__')
	success_url = 'ListaDetalleAdministrador'

#Alta docente
class DocenteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaDocente.html"
	model = Docente
	fields = ('__all__')
	success_url = 'ListaDetalleDocente'

#Disciplinas
class DisciplinasCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="Disciplinas.html"
	model = Disciplinas
	fields = ('__all__')
	success_url = 'ListaDetalleDisciplina'

#Clases
class ClasesCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="Clases.html"
	model = Clase
	fields = ('__all__')
	success_url = '.'

#Disciplinas cursando
class DisciplinasCursandoCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="DisciplinasCursando.html"
	model = Disciplinas_Cursando
	fields = ('__all__')
	success_url = '.'

#Disciplinas cursadas
class DisciplinasCursadasCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="DisciplinasCursadas.html"
	model = Disciplinas_Cursadas
	fields = ('__all__')
	success_url = '.'

#Lista de aspirantes
#class ListaAspiranteListView(ListView):
	"""docstring for ListaAspirante"""
#	model = Datos_Aspirantes


def encabezado (request):
	return render(request,'encabezado.html')

def footer (request):
	return render(request,'footer.html')

def encabezado2 (request):
	return render(request,'encabezado2.html')

def encabezadoE (request):
	return render(request,'encabezadoE.html')


def PublicarAvisos (request):
	return render(request,'PublicarAvisos.html')


def ListaAspirante (request):
	lista = Datos_Aspirantes.objects.filter()
	return render(request,'ListaDetalleAspirante.html',{
		'lista':lista,
		},
		)

	#lista de detalles de docente
def ListaDocente (request):
	listad = Docente.objects.filter()
	return render(request,'ListaDetalleDocente.html',{
		'listad':listad,
		},
		)

	#lista de detalles de administrador
def ListaAdministrador(request):
	listaa = Administrador.objects.filter()
	return render(request,'ListaDetalleAdministrador.html',{
		'listaa':listaa,
		},
		)

	#lista de detalles de estudiante
def ListaEstudiante(request):
	listae = Estudiante.objects.filter()
	return render(request,'ListaDetalleEstudiante.html',{
		'listae':listae,
		},
		)

def ListaDisciplina(request):
	listadi = Disciplinas.objects.filter()
	return render(request,'ListaDetalleDisciplinas.html',{
		'listadi':listadi,
		},
		)

#Actualizar Administrador
class AdministradorUpdateView(UpdateView):
	"""docstring for AspiranteUpdate"""
	template_name="AltaAdministrador.html"
	model = Administrador
	fields = ['Id_Personales',]
	success_url = 'ListaDetalleAdministrador'

