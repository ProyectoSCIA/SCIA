from django.db import models

class Docente(models.Model):
	
	Id_Docente = models.AutoField(
		primary_key = True,
		)

	Id_Aspirante = models.ForeignKey('Datos_Aspirantes',
		on_delete=models.CASCADE,
		)

	Cedula_Profesional = models.CharField(
		max_length=30,
		)

	Tutorado = models.CharField(max_length=30, 
		)

def __str__(self):
		return '%s %s %s' % (self.Id_Aspirante, self.Cedula_Profesional, self.Tutorado)