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
	
	def __str__(self): # __unicode__ en Python 2
		return '%s %s %s %s' % (self.Clave_Disciplina, self.Nombre, self.Grado, self.Grupo)