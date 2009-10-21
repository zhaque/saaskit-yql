from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'yql.views.queries', name='yql-query-list'),
)
