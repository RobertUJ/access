from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('access.apps.citas.views',
    url(r'^citas/$','citas',name='citas_view'),

    url(r'^citas/vuelo/$','citas_vuelo',name='citas_vuelo_view'),
    url(r'^citas/usuario/$','citas_usuario',name='citas_usuario_view'),
    url(r'^citas/confirmada/$','citas_confirmada',name='citas_confirmada_view'),

    url(r'^citas.solicitar/$','crear_cita',name='solicita_citas_view'),
    url(r'^citas.accion/$','accion_citas',name='accion_cita_view'),
    url(r'^citas.editar/(\d{1,6})/$','edita_citas',name='accion_cita_view'),
    url(r'^citas.ver/$','ver_todas_citas',name='ver_todas_citas'),
    url(r'^citas.ver/(\d{1,6})/$','ver_una_cita',name='ver_una_cita'),
   
    url(r'^citas.vuelo/(\d{1,6})/$','add_vuelo',name='add_vuelo'),
    
    url(r'^citas.filtros/$','citas_filtros',name='get_citas_filtros'),
    url(r'^citas.filtros/all$','citas_filtros_all',name='get_citas_filtros_all'),
    
    url(r'^citas.confirma/(\d{1,6})/$','confirma_cita',name='confirma_cita_view'),

    url(r'^citas.calendario/$','calendario_citas',name='calendario_cita'),

)
