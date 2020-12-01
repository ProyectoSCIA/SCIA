from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from base_SCIA import views


urlpatterns=[
path('admin/', admin.site.urls),
url(r'^encabezado/$', views.encabezado),
url(r'^footer/$', views.footer),
#url(r'^home/$', views.home),
#url(r'^login/$', views.login),
url(r'^encabezado2/$', views.encabezado2),
url(r'^encabezadoE/$', views.encabezadoE),
url(r'^AltaAspirante/$', views.DatosAspirantesCreateView.as_view()),
url(r'^AltaDatos/$', views.DatosCreateView.as_view()),
url(r'^AltaDatos/AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),#
#url(r'^AltaDatos/AltaEstudiante/succes/$', views.Guardar3),
url(r'^AltaAdministrador/$', views.AdministradorCreateView.as_view()),
url(r'^AltaAdministrador/succes$', views.Guardar4),
url(r'^AltaDocente/$', views.DocenteCreateView.as_view()),
url(r'^Disciplinas/$', views.DisciplinasCreateView.as_view()),
url(r'^Clases/$', views.ClasesCreateView.as_view()),
url(r'^DisciplinasCursando/$', views.DisciplinasCursandoCreateView.as_view()),
url(r'^DisciplinasCursadas/$', views.DisciplinasCursadasCreateView.as_view()),
url(r'^AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),
url(r'^ListaDetalleAspirante/$', views.ListaDetalleAspirante),
url(r'^ListaDetalleDocente/$', views.ListaDetalleDocente),
#url(r'^Datos_Aspirantes_List/$', views.ListaAspiranteListView.as_view(), name='aspirante-list'),
#url(r'^ListaDetalleDocente/$', views.ListaDetalleDocente),
#url(r'^PublicarAvisos/$', views.PublicarAvisos),
#url(r'^lateral/$', views.lateral),
]