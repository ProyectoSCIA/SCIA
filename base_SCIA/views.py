from django.http import Http404, HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import TemplateView, UpdateView, ListView
from django.urls import reverse_lazy

from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

from base_SCIA.models.datos_aspirantes import Datos_Aspirantes
from base_SCIA.models.datos_procedencia import Datos_Procedencia
from base_SCIA.models.tutor import Tutor
from base_SCIA.models.estudiante import Estudiante
from base_SCIA.models.administrador import Administrador
from base_SCIA.models.docente import Docente
from base_SCIA.models.disciplinas import Disciplinas
from base_SCIA.models.clase import Clase
from base_SCIA.models.disciplinas_cursando import Disciplinas_Cursando

#agregar estudiante
from base_SCIA.forms import EstudianteModelForm
from base_SCIA.forms import AdministradorModelForm
from base_SCIA.forms import DocenteModelForm
from base_SCIA.forms import AspiranteModelForm
from base_SCIA.forms import DisciplinasModelForm

from django.db.models import Q


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


#agregar aspirantes
class DatosAspirantesCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAspirante.html"
	model = Datos_Aspirantes
	form_class = AspiranteModelForm
	success_url = 'ListaDetalleAspirante'

#listar aspirantes
def listar_aspirante(request):
	busqueda = request.POST.get("buscaras") #Recuperamos la busqueda del usuario 
	aspirantes = Datos_Aspirantes.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		aspirantes = Datos_Aspirantes.objects.filter(
			Q(Id_Personales__icontains = busqueda)|
			Q(Nombre__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleAspirante.html', {'aspirantes':aspirantes})


class AspiranteUpdateView(UpdateView):
	"""docstring for AspiranteUpdateView"""
	template_name="EditarAspirante.html"
	model = Datos_Aspirantes
	fields = ('Nombre','Apellido_Paterno','Apellido_Materno','Cargo','Edad','Genero','Telefono','Direccion','Codigo_Postal','CURP','Fecha_Nacimiento','Lugar_Nacimiento','Correo_Electronico','Grupo_Sanguineo',)
	success_url = reverse_lazy('ListaDetalleAspirante')


#datos tutor,procedencia de estudiante
class DatosCreateView(CreateView):
	template_name = 'AltaDatos.html'
	form_class = EstudianteModelForm

	def form_valid(self, form):
		datos_procedencia = form['Datos_Procedencia'].save()
		tutor = form['Tutor'].save(commit=False)
		tutor.datos_procedencia = datos_procedencia
		tutor.save()
		return HttpResponseRedirect('AltaEstudiante.html')

class Guardar2(TemplateView):
	template_name = 'AltaEstudiante.html'

#actualizar datos de procedencia 
class ProcedenciaUpdateView(UpdateView):
	"""docstring for DatosUpdateView"""
	template_name = 'AltaDatos.html'
	model = Datos_Procedencia
	fields = ('Id_Aspirante','Nivel_Basico','Año_Egreso','Promedio_General',)
	success_url = reverse_lazy('ListaDetalleProcedencia')

#Lista de procedencia
def listar_procedencia(request):
	busqueda = request.POST.get("buscarp") #Recuperamos la busqueda del usuario 
	procedencia = Datos_Procedencia.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		procedencia = Datos_Procedencia.objects.filter(
			Q(Id_Procedencia__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleProcedencia.html', {'procedencia':procedencia})


#actualizar datos de  tutor
class TutorUpdateView(UpdateView):
	"""docstring for TutorUpdateView"""
	template_name = 'EditarTutor.html'
	model = Tutor
	fields = ('Id_Aspirante','Nombre_Tutor','Direccion_Tutor','Telefono_Tutor',)
	success_url = reverse_lazy('ListaDetalleTutor')

#Lista de Tutor
def listar_tutor(request):
	busqueda = request.POST.get("buscart") #Recuperamos la busqueda del usuario 
	tutores = Tutor.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		tutores = Tutor.objects.filter(
			Q(Id_Tutor__icontains = busqueda)|
			Q(Nombre_Tutor__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleTutor.html', {'tutores':tutores})



#datos estudiante
class AltaEstudianteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaEstudiante.html"
	model = Estudiante
	fields = ('__all__')
	success_url = 'EstudianteB'

#Actualizar estudiante
class EstudianteUpdateView(UpdateView):
	"""docstring for ActualizarEstudiante"""
	template_name="AltaEstudiante.html"
	model = Estudiante
	fields=('Id_Cursando','Grado','Grupo','Inscrito','Estatus','Promedio_General',)
	success_url = reverse_lazy('EstudianteB')

	#listar un estudiante
def listar_estudiante(request):
	busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
	estudiantes = Estudiante.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		estudiantes = Estudiante.objects.filter(
			Q(NIA__icontains = busqueda)|
			Q(Grado__icontains = busqueda)
		).distinct()

	return render(request, 'EstudianteB.html', {'estudiantes':estudiantes})


	#lista de estudiantes
class DetalleEstudiante(ListView):
	"""docstring for ListaEstudiante"""
	model = Estudiante
	template_name = 'DetalleEstudiante.html'


#Alta admnistrador
class AdministradorCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaAdministrador.html"
	model = Administrador
	form_class = AdministradorModelForm
	success_url = 'ListaDetalleAdministrador'

#Actualizar Administrador
class AdministradorUpdateView(UpdateView):
	"""docstring for AspiranteUpdate"""
	template_name="AltaAdministrador.html"
	model = Administrador
	fields=('Id_Personales',)
	success_url = reverse_lazy('ListaDetalleAdministrador')

def listar_administrador(request):
	busqueda = request.POST.get("buscara") #Recuperamos la busqueda del usuario 
	administradores = Administrador.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		administradores = Administrador.objects.filter(
			Q(Id_Administrador__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleAdministrador.html', {'administradores':administradores})


#Alta docente
class DocenteCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="AltaDocente.html"
	model = Docente
	form_class=DocenteModelForm
	success_url = 'ListaDetalleDocente'

class DocenteUpdateView(UpdateView):
	"""docstring for DocenteUpdateView"""
	template_name="AltaDocente.html"
	model = Docente
	fields=('Id_Aspirante','Grupo_Tutorado',)
	success_url = reverse_lazy('ListaDetalleDocente')

	#listar un docente
def listar_docente(request):
	busqueda = request.POST.get("buscard") #Recuperamos la busqueda del usuario 
	docentes = Docente.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		docentes = Docente.objects.filter(
			Q(Cedula_Profesional__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleDocente.html', {'docentes':docentes})


#lista de docentes
#class ListaDocente(ListView):
#	"""docstring for ListaAspirante"""
#	model = Docente
#	template_name = 'ListaDetalleDocente.html'

#Disciplinas
class DisciplinasCreateView(CreateView):
	"""docstring for DisciplinasCreateView"""
	template_name = "Disciplinas.html"
	model = Disciplinas
	form_class = DisciplinasModelForm
	success_url = 'ListaDetalleDisciplinas'

class DisciplinasUpdateView(UpdateView):
	"""docstring for DisciplinasUpdateView"""
	template_name = "EditarDisciplinas.html"
	model = Disciplinas
	fields = ('Nombre_Disciplina',)
	success_url = reverse_lazy('ListaDetalleDisciplinas')


#Lista de disciplinas
def listar_disciplinas(request):
	busqueda = request.POST.get("buscardi") #Recuperamos la busqueda del usuario 
	disciplinas = Disciplinas.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		disciplinas = Disciplinas.objects.filter(
			Q(Id_Disciplina__icontains = busqueda)|
			Q(Nombre_Disciplina__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleDisciplinas.html', {'disciplinas':disciplinas})




#Disciplinas cursando
class DisciplinasCursandoCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="DisciplinasCursando.html"
	model = Disciplinas_Cursando
	fields = ('__all__')
	success_url = 'ListaDetalleDisciplinasCursando'

#Actualizar Disciplinas cursando
class DisciplinasCursandoUpdateView(UpdateView):
	"""docstring for EstudianteCreateView"""
	template_name="DisciplinasCursando.html"
	model = Disciplinas_Cursando
	fields=('Id_Disciplina','Momento',)
	success_url = reverse_lazy('ListaDetalleDisciplinasCursando')

#lista de disciplinas cursando
def listar_disciplinasCursando(request):
	busqueda = request.POST.get("buscardc") #Recuperamos la busqueda del usuario 
	disciplinasc = Disciplinas_Cursando.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		disciplinasc = Disciplinas_Cursando.objects.filter(
			Q(Id_Cursando__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleDisciplinasCursando.html', {'disciplinasc':disciplinasc})


#Clases
class ClasesCreateView(CreateView):
	"""docstring for EstudianteCreateView"""
	template_name="Clases.html"
	model = Clase
	fields = ('__all__')
	success_url = 'ListaDetalleClases'

#Actualizar Clases
class ClasesUpdateView(UpdateView):
	"""docstring for EstudianteCreateView"""
	template_name="Clases.html"
	model = Clase
	fields=('Id_Disciplina','Id_Docente','Nombre_Clase',)
	success_url = reverse_lazy('ListaDetalleClases')

#lista de clases
def listar_clases(request):
	busqueda = request.POST.get("buscarc") #Recuperamos la busqueda del usuario 
	clases = Clase.objects.all()

	if busqueda: #Preguntando si busqueda está llena 
		clases = Clase.objects.filter(
			Q(Id_Clase__icontains = busqueda)
		).distinct()

	return render(request, 'ListaDetalleClases.html', {'clases':clases})

#reportes
class ReportesView(TemplateView):
	template_name = 'Report.html'

	@method_decorator(csrf_exempt)
	
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'search_report':
				data = []
				start_date = request.POST.get('start_date', '')
				end_date = request.POST.get('end_date', '')
				search = Sale.objects.all()
				if len(start_date) and len(end_date):
					search = search.filter(date_joined__range=[start_date, end_date])
				for s in search:
					data.append([
						s.id,
						s.cli.names,
						s.date_joined.strftime('%Y-%m-%d'),
						format(s.subtotal, '.2f'),
						format(s.iva, '.2f'),
						format(s.total, '.2f'),
					])

				subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
				iva = search.aggregate(r=Coalesce(Sum('iva'), 0)).get('r')
				total = search.aggregate(r=Coalesce(Sum('total'), 0)).get('r')

				data.append([
					'---',
					'---',
					'---',
					format(subtotal, '.2f'),
					format(iva, '.2f'),
					format(total, '.2f'),
				])
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reporte de permisos'

		return context


def encabezado (request):

	print(request.GET)
	return render(request,'encabezado.html')

def footer (request):
	return render(request,'footer.html')

def encabezado2 (request):
	return render(request,'encabezado2.html')

def encabezadoE (request):
	return render(request,'encabezadoE.html')

def Graficos (request):
	return render(request,'Graficos.html')

class DashboardView(TemplateView):
	template_name = 'Graficos.html'

	def calificaciones(self):
		data = []
		try:
			
			for m in range(1, 4):
				total = Disciplinas.objects.filter(Momento=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
				data.append(float(total))
		except:
			pass
		return data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['panel'] = 'Panel de administrador'
		context['calificaciones'] = self.calificaciones()
		return context



def PublicarAvisos (request):
	return render(request,'PublicarAvisos.html')

def lateral1 (request):
	return render(request,'lateral1.html')

def lateral2 (request):
	return render(request,'lateral2.html')

def permisos(request):
	return render(request,'permisos.html')

def PublicarAvisos (request):
	return render(request,'PublicarAvisos.html')

def logout(request):
	# Finalizamos la sesión
	do_logout(request)
	# Redireccionamos a la portada
	return redirect('/home')

def welcome(request):
	# Si estamos identificados devolvemos la portada
	if request.user.is_authenticated:
		return render(request, "bienvenido.html")
	# En otro caso redireccionamos al login
	return redirect('/login')

def login(request):
	# Creamos el formulario de autenticación vacío
	form = AuthenticationForm()
	if request.method == "POST":
		# Añadimos los datos recibidos al formulario
		form = AuthenticationForm(data=request.POST)
		# Si el formulario es válido...
		if form.is_valid():
			# Recuperamos las credenciales validadas
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			# Verificamos las credenciales del usuario
			user = authenticate(username=username, password=password)

			# Si existe un usuario con ese nombre y contraseña
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('/PublicarAvisos')

	# Si llegamos al final renderizamos el formulario
	return render(request, "login.html", {'form': form})

def registrar(request):
	# Creamos el formulario de autenticación vacío
	form = UserCreationForm()
	if request.method == "POST":
		# Añadimos los datos recibidos al formulario
		form = UserCreationForm(data=request.POST)
		# Si el formulario es válido...
		if form.is_valid():

			# Creamos la nueva cuenta de usuario
			user = form.save()

			# Si el usuario se crea correctamente 
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('/PublicarAvisos')

	# Si llegamos al final renderizamos el formulario
	return render(request, "registrar.html", {'form': form})

def bienvenido(request):
	return render(request, "bienvenido.html")

def home (request):
	return render(request,'home.html')

def logout(request):
	# Redireccionamos a la portada
	return redirect('/home')


def PanelEstudiante (request):
	return render(request,'PanelEstudiante.html')

def DatosEstudiante (request):
	return render(request,'DatosEstudiante.html')

def PanelDocente (request):
	return render(request,'PanelDocente.html')

def DatosDocentes (request):
	return render(request,'DatosDocentes.html')

def SubirCalificaciones (request):
	return render(request,'SubirCalificaciones.html')
