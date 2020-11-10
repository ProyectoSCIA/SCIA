from django.db import models

class Disciplinas_Por_Cursar(models.Model):
	
	Id_PorCursar = models.AutoField(
		primary_key = True,
		)

	Clave_Discipina = models.ForeignKey('Disciplinas',
		on_delete=models.CASCADE,
		)

	Nombre = models.CharField(max_length=30, 
		)

	Grado = models.IntegerField( 
		)

	def __str__(self):
		return '%s %s %s' % (self.Clave_Discipina, self.Nombre, self.Grado)