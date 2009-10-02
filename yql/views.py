from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from yql.models import YqlTable, YqlQuery
from yql.search import YqlSearch
import yahoo.yql
import yahoo.application
import settings

def queries(request):
    context_vars = dict()
    context_vars['queries'] = YqlQuery.objects.all()
    if request.method == 'GET':
        query_id = request.GET.get('query', None)
        query_text = request.GET.get('text', None)
        if query_id and query_text:
            query = YqlQuery.objects.get(id=query_id)
            params = query.table.params.all()
            yql = query.query
            if params:
                for param in params:
                    yql += ' and %s=\'%s\'' % (param.name, param.value)

            api = YqlSearch()
            context_vars['result'] = api.fetch(yql % (query.table.name, query_text), query.table.oauth)
    return direct_to_template(request, template="yql/queries.html", extra_context=context_vars)