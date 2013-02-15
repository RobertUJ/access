from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'access.views.home', name='home'),
    # url(r'^access/', include('access.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Our url's apps
    url(r'^static/media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # (r'^comments/', include('django.contrib.comments.urls')),

    #Import urls.py's apps 
    url(r'^',include('access.apps.inicio.urls')),
    url(r'^',include('access.apps.usuarios.urls')),
    url(r'^',include('access.apps.membresias.urls')),
    url(r'^',include('access.apps.citas.urls')),
    url(r'^',include('access.apps.actividades.urls')),

)
