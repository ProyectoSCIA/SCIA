from django.db import models

class Clase(models.Model):
	
	Id_Clase = models.CharField(
		primary_key = True,
		max_length=4,
		)

	Id_Disciplina = models.ForeignKey(
		'Disciplinas',
		on_delete=models.CASCADE,
		)

	Id_Docente = models.ForeignKey(
		'Docente',
		on_delete=models.CASCADE,
		)

	Nombre_Clase = models.CharField(
		max_length=30,
		)



	def __str__(self):
		return '%s' % (self.Id_Clase)