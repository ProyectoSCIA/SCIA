from django.db import models

class Administrador(models.Model):
	
	Id_Administrador = models.CharField(
		primary_key = True,
		max_length=4,
		)

	Id_Personales = models.ForeignKey(
		'Datos_Aspirantes',
		on_delete=models.CASCADE,
	)


	def __str__(self): # __unicode__ en Python 2
		return self.Id_Administrador