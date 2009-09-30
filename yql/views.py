from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from yql.models import YqlTable, YqlQuery
import yahoo.yql

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
            response = yahoo.yql.YQLQuery().execute(yql % (query.table.name, query_text))
            if 'query' in response and 'results' in response['query']:
                context_vars['result'] = response['query']['results']
            elif 'error' in response:
                context_vars['result'] = 'YQL query failed with error: "%s".' % response['error']['description']
            else:
                context_vars['result'] = 'YQL response malformed.'
    return direct_to_template(request, template="yql/queries.html", extra_context=context_vars)