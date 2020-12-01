from django.db import models

class Datos_Procedencia(models.Model):

	Id_Procedencia = models.CharField(
		primary_key = True,
		max_length=4,
	)

	
	Id_Aspirante = models.ForeignKey(
		'Datos_Aspirantes',
		on_delete=models.CASCADE,
	)

	Nivel_Basico = models.CharField(
		max_length = 20,
	)

	Año_Egreso = models.IntegerField(
	)

	Promedio_General  = models.DecimalField (
	max_digits = 5, decimal_places = 2,
	)
	
def __str__(self):
		return '%s %s %s' % (self.Nivel_Basico, self.Año_Egreso, self.Promedio)


