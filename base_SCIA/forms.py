from django.forms import ModelForm

from betterforms.multiform import MultiModelForm

from base_SCIA.models.datos_personales import Datos_Personales
from base_SCIA.models.datos_procedencia import Datos_Procedencia


#from base_SCIA.models.datos_personales_docente import Datos_Personales_Docente
#from base_SCIA.models.docente import Docente

class PersonalesModelForm(ModelForm):
	class Meta:
		model = Datos_Personales
		fields = '__all__'


class ProcedenciaModelForm(ModelForm):
	class Meta:
		model = Datos_Procedencia
		fields = '__all__'


class EstudianteModelForm(MultiModelForm):
	form_classes = {
		'Datos_Personales': PersonalesModelForm,
		'Datos_Procedencia': ProcedenciaModelForm,
	}





#class PersonalesDocentesModelForm(ModelForm):
#	class Meta:
#		model = Datos_Personales_Docente
#		fields = '__all__'


#class DocenteModelForm(ModelForm):
#	class Meta:
#		model = Docente
#		fields = '__all__'


#class DocentesModelForm(MultiModelForm):
#	form_classes = {
#		'Datos_Personales_Docente': PersonalesDocentesModelForm,
#		'Docente': DocenteModelForm,
#	}