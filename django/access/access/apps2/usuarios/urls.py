from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('access.apps.usuarios.views',
	 url(r'^usuarios/registro/$','registro_usuarios',name='registro_usuarios_view'),
     url(r'^usuarios/login/$','login_view',name='view_login'),
     url(r'^usuarios/info.adicional/$','llenar_info_adicional',name='info_adicional_view'),
     url(r'^usuarios/logout/$','logout_view',name='logout_liga_view'),
)
