from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('access.apps.actividades.views',
    url(r'^actividades/$','actividades_all',name='actividades_view'),
    url(r'^actividades.ver/(\d{1,6})$','ver_actividad',name='actividad_view'),
)
