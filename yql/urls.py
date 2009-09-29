from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'yql.views.queries', name='yql-query-list'),
#    url(r'^(?P<slug>[-\w]+)/$', 'livesearch.views.search', name='livesearch_results'),
)
