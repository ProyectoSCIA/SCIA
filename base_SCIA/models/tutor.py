from django.db import models

class Tutor(models.Model):

	id_Tutor = models.AutoField(
    	primary_key = True,
    )

    Matricula = models.ForeignKey(
        'Datos_Academicos',
        on_delete=models.CASCADE,
    )

    Nombre_Completo  = models.CharField(
        max_length = 40,
    )

    Direccion  = models.CharField(
        max_length = 40,
    )

    Telefono = models.IntegerField(
    )
    
     def __str__(self): # __unicode__ en Python 2
        return '%s %s %s' % (self.Matricula, self.Nombre_Completo, self.Direccion, self.Telefono)