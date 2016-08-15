from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns=[
	url(r'^listarvehiculos/registrarvehiculo/$', 'blog.views.registrarvehiculo'),
	url(r'^listarvehiculos/$','blog.views.listarvehiculos'),
	url(r'^iniciosesion/$', 'blog.views.iniciosesion'),
	url(r'^mensaje/$', 'blog.views.mensaje'),
	url(r'^mensaje1/$', 'blog.views.mensaje1'),
	url(r'^nuevousuario/$', 'blog.views.crearusuario'),
	url(r'^cerrarsesion/$', 'blog.views.cerrarsesion'),
	url(r'^modificar/$', 'blog.views.modificar'),
	url(r'^eliminar/$', 'blog.views.eliminar'),
	url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
	url(r'^listVehiculos/$', 'blog.views.listVehiculos'),
]
