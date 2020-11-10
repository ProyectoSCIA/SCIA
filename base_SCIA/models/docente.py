from django.db import models

class Docente(models.Model):
	
	Cedula_Profesional = models.CharField(
		primary_key = True,
		max_length=30,
		)

	Id_Personales_Docente = models.ForeignKey('Datos_Personales_Docente',
		on_delete=models.CASCADE,
		)

	Clave_Disciplina = models.ForeignKey('Disciplinas',
		on_delete=models.CASCADE,
		)

	Cargo = models.CharField(max_length=30, 
		)

	Tutorado = models.CharField(max_length=30, 
		)

def __str__(self):
		return '%s %s %s %s' % (self.Id_Personales_Docente, self.Clave_Disciplina, self.Cargo, self.Tutorado)