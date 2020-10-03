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
]


