from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from base_SCIA import views


urlpatterns=[
path('admin/', admin.site.urls),
url(r'^encabezado/$', views.encabezado),
url(r'^footer/$', views.footer),
url(r'^encabezado2/$', views.encabezado2),
url(r'^encabezadoE/$', views.encabezadoE),
#ASPIRANTES
url(r'^AltaAspirante/$', views.DatosAspirantesCreateView.as_view()),
url(r'^AltaAspirante/ListaDetalleAspirante/$', views.ListaAspirante),
url(r'^ListaDetalleAspirante/$', views.ListaAspirante),
#ESTUDIANTES
url(r'^AltaDatos/$', views.DatosCreateView.as_view()),
url(r'^AltaDatos/AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),
url(r'^AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),
url(r'^ListaDetalleEstudiante/$', views.ListaEstudiante),
#ADMINISTRADOR
url(r'^AltaAdministrador/$', views.AdministradorCreateView.as_view()),
url(r'^AltaAdministrador/ListaDetalleAdministrador/$', views.ListaAdministrador),
url(r'^ListaDetalleAdministrador/$', views.ListaAdministrador),
url(r'^ListaDetalleAdministrador/(?P<pk>\d+)/$', views.AdministradorUpdateView.as_view(), name='AdministradorEditar'),
#DOCENTES
url(r'^AltaDocente/$', views.DocenteCreateView.as_view()),
url(r'^AltaDocente/ListaDetalleDocente/$', views.ListaDocente),
url(r'^ListaDetalleDocente/$', views.ListaDocente),
#DISCIPLINAS
url(r'^Disciplinas/$', views.DisciplinasCreateView.as_view()),
url(r'^Disciplinas/ListaDetalleDisciplinas/$', views.ListaDisciplina),
url(r'^DisciplinasCursando/$', views.DisciplinasCursandoCreateView.as_view()),
url(r'^DisciplinasCursadas/$', views.DisciplinasCursadasCreateView.as_view()),
url(r'^ListaDetalleDisciplinas/$', views.ListaDisciplina),
url(r'^Clases/$', views.ClasesCreateView.as_view()),
url(r'^PublicarAvisos/$', views.PublicarAvisos),
#url(r'^lateral/$', views.lateral),
]