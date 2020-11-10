from django.db import models

class Clase(models.Model):
	
	Id_Clase = models.AutoField(
		primary_key = True,
		)

	Cedula_Profesional = models.ForeignKey('Docente',
		on_delete=models.CASCADE,
		)

	Matricula = models.ForeignKey('Estudiante',
		on_delete=models.CASCADE,
		)

	Clave_Disciplina = models.ForeignKey('Disciplinas',
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return '%s %s %s' % (self.Cedula_Profesional, self.Matricula, self.Clave_Disciplina)