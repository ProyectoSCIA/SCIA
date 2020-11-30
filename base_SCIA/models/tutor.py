
from django.db import models

class Tutor(models.Model):

	Id_Tutor = models.AutoField(
		primary_key = True,
	)

	
	Id_Aspirante = models.ForeignKey(
		'Datos_Aspirantes',
		on_delete=models.CASCADE,
	)

	Nombre_Tutor  = models.CharField(
		max_length = 40,
	)

	Direccion_Tutor  = models.CharField(
		max_length = 40,
	)

	Telefono_Tutor = models.IntegerField(
	)

	def __str__(self):
		return '%s %s %s' % (self.Nombre_Tutor, self.Direccion_Tutor, self.Telefono_Tutor)