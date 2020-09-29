from django.db import models

class Clase(models.Model):
	
    Id_Clase = models.AutoField(
    	primary_key = True,
    	)

    Id_Docente = models.ForeingKey('Docente'
        on_delete=models.CASCADE
    	)

    Id_Estudiante = models.ForeingKey('Estudiante'
        on_delete=models.CASCADE
        )

    Clave_Disciplina = models.ForeingKey('Disciplinas'
        on_delete=models.CASCADE
        )

    def __str__(self): # __unicode__ en Python 2
        return '%s %s %s' % (self.Id_Docente, self.Id_Estudiante, self.Clave_Disciplina)