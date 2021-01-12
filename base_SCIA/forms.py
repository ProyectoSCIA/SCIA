from django.forms import ModelForm

from betterforms.multiform import MultiModelForm

from base_SCIA.models.datos_aspirantes import Datos_Aspirantes
from base_SCIA.models.datos_procedencia import Datos_Procedencia
from base_SCIA.models.tutor import Tutor
from base_SCIA.models.administrador import Administrador
from base_SCIA.models.docente import Docente
from base_SCIA.models.disciplinas import Disciplinas
from base_SCIA.models.estudiante import Estudiante
from django import forms


class ProcedenciaModelForm(ModelForm):
	class Meta:
		model = Datos_Procedencia
		fields= '__all__'

#Clase para agregar un estudiante
class TutorModelForm(ModelForm):
	class Meta:
		model = Tutor
		fields= '__all__'

class EstudianteModelForm(MultiModelForm):
	form_classes = {
		'Datos_Procedencia': ProcedenciaModelForm,
		'Tutor': TutorModelForm,
	}



class AspiranteModelForm(forms.ModelForm):
	class Meta:
		model = Datos_Aspirantes
		fields= [
			'Id_Personales',
			'Nombre',
			'Apellido_Paterno',
			'Apellido_Materno',
			'Cargo','Edad','Genero',
			'Telefono',
			'Direccion',
			'Codigo_Postal',
			'CURP','Fecha_Nacimiento',
			'Lugar_Nacimiento',
			'Correo_Electronico',
			'Grupo_Sanguineo',
		]
		
		labels ={
			'Id_Personales':'Id_Personales',
			'Nombre':'Nombre',
			'Apellido_Paterno':'Apellido_Paterno',
			'Apellido_Materno':'Apellido_Materno',
			'Cargo':'Cargo',
			'Edad':'Edad',
			'Genero':'Genero',
			'Telefono':'Telefono',
			'Direccion':'Direccion',
			'Codigo_Postal':'Codigo_Postal',
			'CURP':'CURP',
			'Fecha_Nacimiento':'Fecha_Nacimiento',
			'Lugar_Nacimiento':'Lugar_Nacimiento',
			'Correo_Electronico':'Correo_Electronico',
			'Grupo_Sanguineo':'Grupo_Sanguineo',
		}

		widgets ={
			'Id_Personales':forms.TextInput(attrs={'class':'form-control'}),
			'Nombre':forms.TextInput(attrs={'class':'form-control'}),
			'Apellido_Paterno' : forms.TextInput(attrs={'class':'form-control'}),
			'Apellido_Materno' : forms.TextInput(attrs={'class':'form-control'}),
			'Cargo' : forms.TextInput(attrs={'class':'form-control'}),
			'Edad' : forms.TextInput(attrs={'class':'form-control'}),
			'Genero' : forms.TextInput(attrs={'class':'form-control'}),
			'Telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'Direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'Codigo_Postal' : forms.TextInput(attrs={'class':'form-control'}),
			'CURP' : forms.TextInput(attrs={'class':'form-control'}),
			'Fecha_Nacimiento' : forms.TextInput(attrs={'class':'form-control'}),
			'Lugar_Nacimiento' : forms.TextInput(attrs={'class':'form-control'}),
			'Correo_Electronico' : forms.TextInput(attrs={'class':'form-control'}),
			'Grupo_Sanguineo' : forms.TextInput(attrs={'class':'form-control'}),

		}

class AdministradorModelForm(forms.ModelForm):
	class Meta:
		model = Administrador
		fields= [
			'Id_Administrador',
			'Id_Personales',
		]
		
		labels ={
			'Id_Administrador':'Id_Administrador',
			'Id_Personales' : 'Id_Personales',
		}
		
		widgets ={
			'Id_Administrador':forms.TextInput(attrs={'class':'form-control'}),
			'Id_Personales' : forms.Select(attrs={'class':'form-control'}),

		}

class DocenteModelForm(forms.ModelForm):
	class Meta:
		model = Docente
		fields= [
			'Cedula_Profesional',
			'Id_Aspirante',
			'Grupo_Tutorado',
		]
		
		labels ={
			'Cedula_Profesional':'Cedula_Profesional',
			'Id_Aspirante':'Id_Aspirante',
			'Grupo_Tutorado':'Grupo_Tutorado',
		}
		
		widgets ={
			'Cedula_Profesional':forms.TextInput(attrs={'class':'form-control'}),
			'Id_Aspirante' : forms.Select(attrs={'class':'form-control'}),
			'Grupo_Tutorado' : forms.TextInput(attrs={'class':'form-control'}),

		}

class DisciplinasModelForm(forms.ModelForm):
	class Meta:
		model = Disciplinas
		fields= [
			'Id_Disciplina',
			'Nombre_Disciplina',
		]
		
		labels ={
			'Id_Disciplina':'Id_Disciplina',
			'Nombre_Disciplina':'Nombre_Disciplina',
		}
		
		widgets ={
			'Id_Disciplina':forms.TextInput(attrs={'class':'form-control'}),
			'Nombre_Disciplina':forms.TextInput(attrs={'class':'form-control'}),

		}
