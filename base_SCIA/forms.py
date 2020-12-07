from django.forms import ModelForm

from betterforms.multiform import MultiModelForm

from base_SCIA.models.datos_aspirantes import Datos_Aspirantes
from base_SCIA.models.datos_procedencia import Datos_Procedencia
from base_SCIA.models.tutor import Tutor
from django import forms


#Clase pafa agregar un aspirante


#Clase para agregar un estudiante
class TutorModelForm(ModelForm):
	class Meta:
		model = Tutor
		fields= '__all__'
# estilo Usando los 
#		fields = 'Id_Personales','Nombre', 'Apellido_Paterno', 'Apellido_Materno','Edad', 'Genero', 'Telefono', 'Direccion', 'Codigo_Postal','CURP', 'Fecha_Nacimiento', 'Lugar_Nacimiento', 'Correo_Electronico', 'Grupo_Sanguineo'

class ProcedenciaModelForm(ModelForm):
	class Meta:
		model = Datos_Procedencia
		fields= '__all__'
# estilo Usando los 
#		fields = 'Id_Procedencia', 'Nivel_Basico', 'Año_Egreso', 'Promedio'

class EstudianteModelForm(MultiModelForm):
	form_classes = {
		'Datos_Procedencia': ProcedenciaModelForm,
		'Tutor': TutorModelForm,
	}



class AspiranteModelForm(forms.ModelForm):
	class Meta:
		model = Datos_Aspirantes
		fields= '__all__'




