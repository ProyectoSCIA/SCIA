from django.db import models

class Tutor(models.Model):

	id_Tutor = models.AutoField(
		primary_key = True,
	)

	Matricula = models.ForeignKey(
		'Estudiante',
		on_delete=models.CASCADE,
	)

	Nombre_CompletoT  = models.CharField(
		max_length = 40,
	)

	DireccionT  = models.CharField(
		max_length = 40,
	)

	TelefonoT = models.IntegerField(
	)
	
	def __str__(self):
		return '%s %s %s %s' % (self.Matricula, self.Nombre_CompletoT, self.DireccionT, self.TelefonoT)