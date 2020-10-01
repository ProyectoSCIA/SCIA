from django.contrib import admin
from base_SCIA import models

# Register your models here.

admin.site.register(models.Administrador)
admin.site.register(models.Clase)
admin.site.register(models.Datos_Docente)
admin.site.register(models.Datos_Personales_Docente)
admin.site.register(models.Disciplinas)
admin.site.register(models.Disciplinas_Cursadas)
admin.site.register(models.Disciplinas_Por_Cursar)
admin.site.register(models.Docente)
admin.site.register(models.Datos_Academicos)
admin.site.register(models.Datos_Personales)
admin.site.register(models.Datos_Procedencia)
admin.site.register(models.Disciplinas_Cursando)
admin.site.register(models.Estudiante)
admin.site.register(models.Login)
admin.site.register(models.Tutor)
