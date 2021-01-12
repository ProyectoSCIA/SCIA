from django.db import models

class Estudiante(models.Model):

	NIA = models.CharField(
		primary_key = True,
		max_length = 8,
		)

	Id_Tutor = models.ForeignKey(
		'Tutor',
		on_delete=models.CASCADE,
		)

	Id_Procedencia = models.ForeignKey(
		'Datos_Procedencia',
		on_delete=models.CASCADE,
		)
	
	Id_Cursando = models.ForeignKey(
		'Disciplinas_Cursando',
		on_delete=models.CASCADE,
		)

	Grado = models.IntegerField(
		)

	Grupo = models.CharField(
			max_length = 2,
		)

	Inscrito = models.CharField(
			max_length = 2,
		)

	Estatus = models.CharField(
			max_length = 10,
		)

	Promedio_General = models.DecimalField (
		max_digits = 5, decimal_places = 2,
		)

	def __str__(self):
		return self.NIA
