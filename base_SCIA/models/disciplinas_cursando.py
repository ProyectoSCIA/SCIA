from django.db import models

class Disciplinas_Cursando(models.Model):


	Id_Cursando = models.AutoField(
		primary_key = True,
	)

	Clave_Disciplina = models.ForeignKey(
		'Disciplinas',
		on_delete=models.CASCADE,
	)

	Nombre = models.CharField(
		max_length = 40,
	)

	Grado = models.IntegerField(
	)

	Grupo = models.CharField(
		max_length = 2,
	)
	
	Momento1 = models.DecimalField (
		max_digits = 5, decimal_places = 2,
	)
	
	Momento2 = models.DecimalField (
		max_digits = 5, decimal_places = 2,
	
	)
	
	Momento3 = models.DecimalField (
		max_digits = 5, decimal_places = 2,
	)
	
	Calificacion_Final = models.DecimalField (
		max_digits = 5, decimal_places = 2,
	)
	
	def __str__(self):
		return '%s %s %s %s %s %s %s %s' % (self.Clave_Disciplina, self.Nombre, self.Grado, 
			self.Grupo, self.Momento1, self.Momento2, self.Momento3, self.Calificacion_Final)