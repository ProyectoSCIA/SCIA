from django.db import models

class Administrador(models.Model):
	
    Id_Administrador = models.AutoField(
    	primary_key = True,
    	)

    Nombre_Completo = models.CharField(max_length=40, 
    	)

    Cargo = models.CharField(max_length=30, 
    	)

    Genero = models.CharField(max_length=2, 
        )

    Edad = models.IntegerField( 
        )

    Telefono = models.IntegerField( 
        )

    Direccion = models.CharField(max_length=60, 
        )

    Codigo_Postal = models.IntegerField( 
        )

    Correo_Electronico = models.EmailField(
    )
   
    Grupo_Sanguineo = models.CharField(max_length=3, 
        )


    def __str__(self): # __unicode__ en Python 2
        return '%s %s %s %s %s %s %s %s %s' % (self.Nombre_Completo, self.Cargo, self.Genero,
            self.Edad, self.Telefono, self.Direccion, self.Codigo_Postal, self.Correo_Electronico, self.Grupo_Sanguineo)