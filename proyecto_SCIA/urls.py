from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from base_SCIA import views
from django.urls import reverse_lazy



urlpatterns=[
path('admin/', admin.site.urls),
url(r'^encabezado/$', views.encabezado),
url(r'^footer/$', views.footer),
url(r'^encabezado2/$', views.encabezado2),
url(r'^encabezadoE/$', views.encabezadoE),
#ASPIRANTES
url(r'^AltaAspirante/$', views.DatosAspirantesCreateView.as_view()),
url(r'^AltaAspirante/ListaDetalleAspirante/$', views.listar_aspirante),
url(r'^ListaDetalleAspirante/$', views.listar_aspirante, name='ListaDetalleAspirante'),
url(r'^AltaAspirante/(?P<pk>\d+)/$',views.AspiranteUpdateView.as_view(), name= 'EditarAspirante'),
#ESTUDIANTES
url(r'^AltaDatos/$', views.DatosCreateView.as_view()),
url(r'^AltaDatos/AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),
url(r'^AltaDatos/Guardar2/EstudianteB/$', views.listar_estudiante, name='EstudianteB'),

url(r'^ListaDetalleProcedencia/$', views.listar_procedencia, name='ListaDetalleProcedencia'),
url(r'^AltaDatos/(?P<pk>\d+)/$', views.ProcedenciaUpdateView.as_view(), name='ProcedenciaEditar'),

url(r'^ListaDetalleTutor/$', views.listar_tutor, name='ListaDetalleTutor'),
url(r'^ListaDetalleTutor/(?P<pk>\d+)/$', views.TutorUpdateView.as_view(), name='TutorEditar'),


url(r'^EstudianteB/$', views.listar_estudiante, name='EstudianteB'),
url(r'^AltaEstudiante/$', views.AltaEstudianteCreateView.as_view()),
#url(r'^ListaDetalleEstudiante/$', views.ListaEstudiante.as_view(), name='ListaDetalleEstudiante'),
url(r'^DetalleEstudiante/$', views.DetalleEstudiante.as_view(), name='DetalleEstudiante'),
url(r'^AltaEstudiante/EstudianteB/$', views.listar_estudiante, name='EstudianteB'),
url(r'^ListaDetalleEstudiante/(?P<pk>\d+)/$', views.EstudianteUpdateView.as_view(), name='EstudianteEditar'),
#ADMINISTRADOR
url(r'^AltaAdministrador/$', views.AdministradorCreateView.as_view()),
url(r'^AltaAdministrador/ListaDetalleAdministrador/$', views.listar_administrador),
url(r'^ListaDetalleAdministrador/$', views.listar_administrador, name='ListaDetalleAdministrador'),
url(r'^AltaAdministrador/(?P<pk>\d+)/$', views.AdministradorUpdateView.as_view(), name='AdministradorEditar'),
#DOCENTES
url(r'^AltaDocente/$', views.DocenteCreateView.as_view()),
url(r'^AltaDocente/ListaDetalleDocente/$', views.listar_docente),
url(r'^ListaDetalleDocente/$', views.listar_docente, name='ListaDetalleDocente'),
url(r'^AltaDocente/(?P<pk>\w+)/$', views.DocenteUpdateView.as_view(), name='DocenteEditar'),
#DISCIPLINAS
url(r'^Disciplinas/$', views.DisciplinasCreateView.as_view()),
url(r'^Disciplinas/ListaDetalleDisciplinas/$', views.listar_disciplinas),
url(r'^ListaDetalleDisciplinas/$', views.listar_disciplinas, name='ListaDetalleDisciplinas'),
url(r'^Disciplinas/(?P<pk>\w+)/$', views.DisciplinasUpdateView.as_view(), name='DisciplinasEditar'),
#Disciplinas cursando
url(r'^DisciplinasCursando/$', views.DisciplinasCursandoCreateView.as_view()),
url(r'^DisciplinasCursando/ListaDetalleDisciplinasCursando/$', views.listar_disciplinasCursando),
url(r'^ListaDetalleDisciplinasCursando/$', views.listar_disciplinasCursando, name='ListaDetalleDisciplinasCursando'),
url(r'^DisciplinasCursando/(?P<pk>\d+)/$', views.DisciplinasCursandoUpdateView.as_view(), name='DisciplinasCursandoEditar'),
#CLASES
url(r'^Clases/$', views.ClasesCreateView.as_view()),
url(r'^Clases/ListaDetalleClases/$', views.listar_clases),
url(r'^ListaDetalleClases/$', views.listar_clases, name='ListaDetalleClases'),
url(r'^Clases/(?P<pk>\d+)/$', views.ClasesUpdateView.as_view(), name='ClasesEditar'),

#url(r'^lateral/$', views.lateral),
url(r'^home/$', views.home),
url(r'^lateral1/$', views.lateral1),
url(r'^lateral2/$', views.lateral2),
url(r'^PublicarAvisos/$', views.PublicarAvisos),
url(r'^permisos/$', views.permisos),
path('', views.bienvenido),
path('registrar', views.registrar),
path('login', views.login),
path('logout', views.logout),

path('PanelEstudiante/', views.PanelEstudiante),
path('DatosEstudiante/', views.DatosEstudiante),
path('PanelDocente/', views.PanelDocente),
path('DatosDocentes/', views.DatosDocentes),
path('SubirCalificaciones/', views.SubirCalificaciones),



path('Report', views.ReportesView.as_view(), name ='reporte'),


url(r'^Graficos/$', views.Graficos),

]
