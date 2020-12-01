from django.db import models

class Disciplinas_Cursando(models.Model):


	Id_Cursando = models.CharField(
		primary_key = True,
		max_length=4,
	)

	Id_Disciplina = models.ForeignKey(
		'Disciplinas',
		on_delete=models.CASCADE,
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
	
	
	def __str__(self):
		return '%s %s %s %s ' % (self.Id_Disciplina, self.Momento1,
		 self.Momento2, self.Momento3)