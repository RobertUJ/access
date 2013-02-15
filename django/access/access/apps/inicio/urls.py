from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('access.apps.inicio.views',
	url(r'^$', 'inicio',name='vista_inicio'),
    url(r'^contact/$','contact_view',name='contact_view'),

)