from django.db import models

class Administrador(models.Model):
	
	Id_Administrador = models.AutoField(
		primary_key = True,
		)

	Id_Personales = models.ForeignKey(
		'Datos_Aspirantes',
		on_delete=models.CASCADE,
	)


	def __str__(self): # __unicode__ en Python 2
		return '%s ' % (self.Id_Personales)