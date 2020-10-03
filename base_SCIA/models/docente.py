from django.db import models

class Docente(models.Model):
	
	Id_Docente = models.AutoField(
		primary_key = True,
		)

	Id_Personales_Docente = models.ForeignKey('Datos_Personales_Docente',
		on_delete=models.CASCADE,
		)

	Cedula_Personal = models.ForeignKey('Datos_Docente',
		on_delete=models.CASCADE,
		)

	Clave_Disciplina = models.ForeignKey('Disciplinas',
		on_delete=models.CASCADE,
		)

def __str__(self):
		return '%s %s %s' % (self.Id_Personales_Docente, self.Cedula_Personal, self.Clave_Disciplina)