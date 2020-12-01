from django.db import models

class Disciplinas_Cursadas(models.Model):
	
	Id_Cursadas = models.CharField(
		primary_key = True,
		max_length=4,
		)

	Id_Discipina = models.ForeignKey(
		'Disciplinas',
		on_delete=models.CASCADE,
		)

	Nombre_Cursadas = models.CharField(
		max_length=30,
		)

	Calificacion = models.DecimalField (
		max_digits = 5, decimal_places = 2,
		)

def __str__(self):
		return '%s %s %s' % (self.Id_Discipina, self.Nombre_Cursadas, self.Calificacion)