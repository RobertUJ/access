from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('access.apps.membresias.views',
	url(r'^membresia.compra/tipo/$', 'sel_tipo_mem',name='tipo_mem_view'),
	
	url(r'^membresia.compra/online$', 'compra_membresia_online',name='compra_membresia_online'),
	url(r'^membresia.compra/callcenter/$', 'compra_membresia_call_center',name='compra_membresia_callcenter'),
	
	url(r'^membresia.compra/cantidad/$', 'compra_cantidad',name='compra_cantidad_view'),
	url(r'^membresia.compra/(\d{1,6})/$', 'compra_multiple',name='compra_mem_multiple'),
	
	url(r'^membresia.referidos/$', 'referidos_vista',name='ver_referidos'),
	url(r'^membresia.compra/referido/$', 'compra_referido',name='compra_referido_view'),
	
	url(r'^membresia.compra/seltipo/(\d{1,6})/$', 'mem_tipo',name='mem_tipo_view'),
	url(r'^membresia.resumen/$','resumen_compra',name='resumen_compra_view'),
	url(r'^membresia.inicio/$','activa_membresia_login',name='inicio_membresia_view'),
	url(r'^membresia.activa/$','activa_membresia_update',name='activa_membresia_update_view'),
	
	url(r'^membresia.menor/$','menores_edad_all',name='menores_edad_view'),
	url(r'^membresia.menor/nuevo/$','menores_edad_nuevo',name='menores_edad_nuevo'),
	
	url(r'^membresia.menor/pase/$','compra_pase',name='compra_pase_view'),
	
	# Edicion de perfil
	url(r'^membresia.edicion/$','edit_mem',name='edicion_membresia'),
	url(r'^membresia.edicion/pass$','reset_pass',name='reset_pass'),


)