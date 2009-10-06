from django.conf.urls.defaults import *
from lingcod.spacing.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', Index),
    (r'^land/kml/', LandKML),
    (r'^fish_distance/kml', FishDistanceKML),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/pydevWorkspace/reporting_dev/media', 'show_indexes': False}),
    (r'^tests/', 'django.views.generic.simple.direct_to_template', {'template': 'common/tests.html'}),
    (r'^layers/', include('lingcod.layers.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)