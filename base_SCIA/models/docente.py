from django.db import models

class Docente(models.Model):

	Cedula_Profesional = models.CharField(
		primary_key = True,
		max_length=20,
		)

	Id_Aspirante = models.ForeignKey('Datos_Aspirantes',
		on_delete=models.CASCADE,
		)

	Grupo_Tutorado = models.CharField(max_length=30, 
		)

	def __str__(self):
		return '%s ' % (self.Cedula_Profesional)