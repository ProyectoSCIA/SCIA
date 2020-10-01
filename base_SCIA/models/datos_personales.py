from django.db import models

class Datos_Personales(models.Model):

   Id_Personales = models.AutoField(
    	primary_key = True,
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
   
   Edad = models.IntegerField(
    )
   
   Genero = models.CharField(
        max_length = 2,
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
   
   Fecha_Nacimiento = models.DateTimeField(
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
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.Nombre, self.Apellido_Paterno, self.Apellido_Materno, 
          self.Edad, self.Genero, self.Telefono, self.Direccion, self.Codigo_Postal, 
          self.CURP, self.Fecha_Nacimiento, self.Lugar_Nacimiento, self.Correo_Electronico, self.Grupo_Sanguineo)








