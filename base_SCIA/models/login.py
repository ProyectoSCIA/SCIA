from django.db import models

class Login(models.Model):

	Id_Login = models.AutoField(
	primary_key = True,
	)

	Usuario = models.CharField(
	 max_length = 20,
	)

	Contraseña = models.CharField(
	max_length = 20,
	)


	def __str__(self): # __unicode__ en Python 2
	 return '%s %s' % (self.Usuario , self.Contraseña)