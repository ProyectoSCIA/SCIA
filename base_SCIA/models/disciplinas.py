from django.db import models

class Disciplinas(models.Model):
	
	Clave_Disciplina = models.AutoField(
		primary_key = True, 
		)

	Id_Cursando = models.ForeignKey(
		'Disciplinas_Cursando',
		on_delete=models.CASCADE,
	)

	Nombre = models.CharField(
		max_length=30, 
		)

	Calificacion =models.DecimalField (
		max_digits = 5, 
		decimal_places = 2,
		)

	Acreditacion = models.IntegerField(
		)

def __str__(self):
		return '%s %s %s %s' % (self.Id_Cursando, self.Nombre, self.Calificacion, self.Acreditacion)