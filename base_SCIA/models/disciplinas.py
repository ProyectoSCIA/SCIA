from django.db import models

class Disciplinas(models.Model):
	
    Clave_Disciplina = models.AutoField(
    	primary_key = True,
    	)

    Nombre = models.CharField(max_length=30, 
    	)

    Calificacion =models.DecimalField (
        ..., max_digits = 5, decimal_places = 2
        )

    Acreditacion = models.IntegerField(
    	)

def __str__(self):
        return "("+str(self.Nombre) + "," +str(self.Calificacion)+ ","+str(self.Acreditacion)+")"