from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_image, name='addImage'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^images/$', views.index, name='images'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^isLogged/$', views.islogged_view, name='isLogged'),
    url(r'^verImagenes', views.ver_imagenes, name='verImagenes'),
    url(r'^agregarImagen', views.agregar_imagen, name='agregarImagen'),
    url(r'^agregarUsuario', views.agregar_usuario, name='agreagarUsuario'),
    url(r'^ingresar', views.ingresar, name='ingresar'),
]