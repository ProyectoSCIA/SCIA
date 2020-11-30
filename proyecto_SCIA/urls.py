from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from base_SCIA import views


urlpatterns=[
path('admin/', admin.site.urls),
url(r'^encabezado/$', views.encabezado),
url(r'^footer/$', views.footer),
url(r'^home/$', views.home),
url(r'^login/$', views.login),
url(r'^encabezado2/$', views.encabezado2),
url(r'^encabezadoE/$', views.encabezadoE),
url(r'^AltaAspirante/$', views.DatosAspirantesCreateView.as_view()),
url(r'^AltaAspirante/Menu$', views.Menu1),
#url(r'^AltaAspirante/AltaDatos/$', views.EstudianteCreateView.as_view()),
#url(r'^AltaAspirante/AltaDatos/AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),
#url(r'^AltaAspirante/AltaDatos/AltaEstudiante/succes/$', views.Guardar3),
#url(r'^AltaAspirante/AltaAdministrador/$', views.AdministradorCreateView.as_view()),
url(r'^AltaAdministrador/$', views.AdministradorCreateView.as_view()),
url(r'^ListaDetalleEstudiante/$', views.ListaDetalleEstudiante),
url(r'^DatosPersonalesEstudiante/$', views.DatosPersonalesEstudiante),
url(r'^DatosAcademicosEstudiante/$', views.DatosAcademicosEstudiante),
url(r'^DatosProcedenciaEstudiante/$', views.DatosProcedenciaEstudiante),
#url(r'^AltaDocente/$', views.DocenteCreateView.as_view()),
url(r'^ListaDetalleDocente/$', views.ListaDetalleDocente),
url(r'^DatosPersonalesDocente/$', views.DatosPersonalesDocente),
url(r'^DatosAcademicosDocente/$', views.DatosAcademicosDocente),
url(r'^PublicarAvisos/$', views.PublicarAvisos),
url(r'^lateral/$', views.lateral),
#url(r'^AgregarEstudiante/$', views.EstudianteCreateView.as_view()),
]