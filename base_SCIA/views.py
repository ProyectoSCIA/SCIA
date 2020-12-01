from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import ListView

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

#agregar aspirantes
class DatosAspirantesCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAspirante.html"
	model = Datos_Aspirantes
	fields = ('__all__')
	success_url = '.'

#datos tutor procedencia estudiante
class DatosCreateView(CreateView):
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
	success_url = '.'

#Alta admnistrador
class AdministradorCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAdministrador.html"
	model = Administrador
	fields = ('__all__')
	success_url = 'succes'

class Guardar4(TemplateView):
	template_name = 'succes.html'

#Alta docente
class DocenteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaDocente.html"
	model = Docente
	fields = ('__all__')
	success_url = '.'

#Disciplinas
class DisciplinasCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="Disciplinas.html"
	model = Disciplinas
	fields = ('__all__')
	success_url = '.'

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
class ListaAspiranteListView(ListView):
	"""docstring for ListaAspirante"""
	model = Datos_Aspirantes
	paginate_by = 20

	def get_queryset(self):
		queryset = super(ListaAspiranteListView, self).get_queryset()
		return queryset.filter(Nombre=True)

def encabezado (request):
	return render(request,'encabezado.html')

def footer (request):
	return render(request,'footer.html')

def encabezado2 (request):
	return render(request,'encabezado2.html')

def encabezadoE (request):
	return render(request,'encabezadoE.html')

def ListaDetalleAspirante (request):
	lista = Datos_Aspirantes.objects.filter()
	lista2 = Datos_Procedencia.objects.filter()
	return render(request,'ListaDetalleAspirante.html',{
		'lista':lista,
		'lista2':lista2,
		},
		)

	#lista de detalles de docente
def ListaDetalleDocente (request):
	lista = Datos_Aspirantes.objects.filter()
	lista2 = Datos_Procedencia.objects.filter()
	return render(request,'ListaDetalleAspirante.html',{
		'lista':lista,
		'lista2':lista2,
		},
		)