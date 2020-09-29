from django.db import models

class Datos_Docente(models.Model):

    Cedula_Personal = models.AutoField(
    	primary_key = True,
    	)

    Cargo = models.CharField(max_length=30, 
    	)

    Disciplinas_Asignadas = models.CharField(max_length=30, 
    	)

    Tutorado = models.CharField(max_length=30, 
    	)

    def __str__(self):
        return '%s %s %s' % (self.cargo, self.Disciplinas_Asignadas, self.Tutorado)