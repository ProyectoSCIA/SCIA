from django.db import models

class Estudiante(models.Model):

	Id_Estudiante = models.AutoField(
		primary_key = True,
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

	Id_Cursadas = models.ForeignKey(
		'Disciplinas_Cursadas',
		on_delete=models.CASCADE,
	)

	Matricula = models.IntegerField(

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
		return '%s %s %s %s %s %s %s %s %s %s %s' % (self.Id_Aspirante, self.Id_Tutor,
			self.Id_Procedencia, self.Id_Cursando, self.Id_Cursandas, self.Matricula,
			 self.Grado, self.Grupo, self.Inscrito,
			 self.Estatus, self.Promedio_General)