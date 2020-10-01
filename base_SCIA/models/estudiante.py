from django.db import models

class Estudiante(models.Model):


	Id_Estudiante = models.AutoField(
		primary_key = True,
	)

	Id_Personales = models.ForeignKey('Datos_Personales',
		on_delete=models.CASCADE
	)
	
	Id_Cursando = models.ForeignKey(
		'Disciplinas_Cursando',
		on_delete=models.CASCADE,
	)
	
	Id_Tutor = models.ForeignKey(
		'Tutor',
		on_delete=models.CASCADE,
	)
	
	Id_Procedencia = models.ForeignKey(
		'Datos_Procedencia',
		on_delete=models.CASCADE,
	)
	
	Matricula = models.ForeignKey(
		'Datos_Academicos',
		on_delete=models.CASCADE,
	)

def __str__(self): # __unicode__ en Python 2
		return '%s %s %s %s %s' % (self.Id_Personales, self. Id_Cursando, self.Id_Tutor, self.Id_Procedencia, self.Matricula)