from django.db import models

class Datos_Aspirantes(models.Model):

	Id_Personales = models.CharField(
			primary_key = True,
			max_length=4,
		)
	Nombre = models.CharField(
				max_length = 20,
		)

	Apellido_Paterno = models.CharField(
				max_length = 20,
		)
	
	Apellido_Materno = models.CharField(
				max_length = 20,
		)
	
	Cargo= models.CharField(
		max_length = 20,
		)

	Edad = models.IntegerField(
		)
	
	Genero = models.CharField( max_length=2,
		)
	
	Telefono = models.IntegerField(
		)
	
	Direccion = models.CharField(
				max_length = 40,
		)
	
	Codigo_Postal  = models.IntegerField(
		)
	
	CURP = models.CharField(
				max_length = 20,
		)
	
	Fecha_Nacimiento = models.DateField(
		max_length = 40,
		)
	
	Lugar_Nacimiento = models.CharField(
				max_length = 40,
		)
	
	Correo_Electronico = models.EmailField(
		)
	
	Grupo_Sanguineo = models.CharField(
				max_length = 2,
		)

	def __str__(self):
		return '%s %s ' % (self.Id_Personales, self.Nombre)








