from django.db import models

class Datos_Academicos(models.Model):

	Matricula = models.IntegerField(
	        primary_key= True, 
	        default="",
	    )

	Id_Estudiante = models.ForeignKey(
	        'Estudiante',
	        on_delete=models.CASCADE,
	    )

	Grado = models.IntegerField(
	    )

	Grupo = models.CharField(
	        max_length = 2,
	    )

	Inscrito = models.CharField(
	        max_length = 2,
	    )

	Estatus = models.CharField(
	        max_length = 10,
	    )

	Promedio_General = models.DecimalField (
		..., max_digits = 5, decimal_places = 2,
	    )
	    


def __str__(self):
        return '%s %s %s %s %s ' % (self.Grado, self.Grupo, self.Inscrito, self.Estatus, self.Promedio_General)