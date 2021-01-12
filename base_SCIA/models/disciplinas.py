from django.db import models

class Disciplinas(models.Model):

	Id_Disciplina = models.CharField(
		primary_key = True, 
		max_length=4,
		)

	Nombre_Disciplina = models.CharField(
		max_length=30, 
		)


	def __str__(self):
		return '%s %s' % (self.Id_Disciplina, self.Nombre_Disciplina)