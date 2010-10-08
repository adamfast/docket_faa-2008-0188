from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<n_number>[a-zA-Z0-9*.]+)/$', 'aircraftreregistration.views.find_dates'),

    (r'^$', 'aircraftreregistration.views.index'),
)
