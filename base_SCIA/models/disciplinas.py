from django.db import models

class Disciplinas(models.Model):
	
	Id_Disciplina = models.AutoField(
		primary_key = True, 
		)

	Clave_Disciplina = models.CharField(
		max_length=30,
		)

	Nombre_Disciplina = models.CharField(
		max_length=30, 
		)


def __str__(self):
		return '%s %s ' % (self.Clave_Disciplina, self.Nombre_Disciplina)