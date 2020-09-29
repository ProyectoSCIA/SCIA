
from django.db import models

class Datos_Procedencia(models.Model):

	Id_Procedencia = models.AutoField(
    	primary_key = True,
    )

	Nivel_Basico = models.CharField(
        max_length = 20,
    )

	Año_Egreso = models.IntegerField(
    )

	Promedio  = models.DecimalField (
	..., max_digits = 5, decimal_places = 2
    )
    
      def __str__(self): # __unicode__ en Python 2
        return '%s %s %s' % (self.Nivel_Basico, self.Año_Egreso, self.Promedio)


