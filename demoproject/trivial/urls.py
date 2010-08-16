from django.conf.urls.defaults import *

urlpatterns = patterns('secure.views',
    (r'^$', 'homepage'),
)
