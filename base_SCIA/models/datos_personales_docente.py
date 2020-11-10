from django.db import models

class Datos_Personales_Docente(models.Model):

	Id_Personales_Docente = models.AutoField(
		primary_key = True,
		)

	Nombre_Completo = models.CharField(max_length=60, 
		)

	Genero = models.CharField(max_length=2, 
		)

	Edad = models.IntegerField(
		)

	Telefono = models.IntegerField(
		)

	DireccionD = models.CharField(max_length=60, 
		)

	Codigo_Postal = models.IntegerField( 
		)

	Correo_Electronico = models.EmailField(
	)

	Grupo_Sanguineo = models.CharField(max_length=3, 
		)

def __str__(self):
		return '%s %s %s %s %s %s %s %s' % (self.Nombre_Completo, self.Genero, self.Edad,
		self.Telefono, self.DireccionD, self.Codigo_Postal,
		self.Correo_Electronico, self.Grupo_Sanguineo)