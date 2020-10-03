from django.db import models

class Clase(models.Model):
	
	Id_Clase = models.AutoField(
		primary_key = True,
		)

	Id_Docente = models.ForeignKey('Docente',
		on_delete=models.CASCADE,
		)

	Id_Estudiante = models.ForeignKey('Estudiante',
		on_delete=models.CASCADE,
		)

	Clave_Disciplina = models.ForeignKey('Disciplinas',
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return '%s %s %s' % (self.Id_Docente, self.Id_Estudiante, self.Clave_Disciplina)