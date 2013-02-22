from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('access.apps.membresias.views',
	url(r'^membresia.compra/tipo/$', 'sel_tipo_mem',name='tipo_mem_view'),
	
	url(r'^membresia.compra/online$', 'compra_membresia_online',name='compra_membresia_online'),
	url(r'^membresia.compra/callcenter/$', 'compra_membresia_call_center',name='compra_membresia_callcenter'),
	
	url(r'^membresia.referidos/$', 'referidos_vista',name='ver_referidos'),
	url(r'^membresia.compra/referido/$', 'compra_referido',name='compra_referido_view'),
	
	url(r'^membresia.compra/seltipo/(\d{1,6})/$', 'mem_tipo',name='mem_tipo_view'),
	url(r'^membresia.resumen/$','resumen_compra',name='resumen_compra_view'),
	url(r'^membresia.inicio/$','activa_membresia_login',name='inicio_membresia_view'),
	url(r'^membresia.activa/$','activa_membresia_update',name='activa_membresia_update_view'),

)