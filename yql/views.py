from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from yql.models import YqlTable, YqlQuery#, YqlSearch

def queries(request):
    context_vars = dict()
    context_vars['queries'] = YqlQuery.objects.all()
    if request.method == 'GET':
        query_id = request.GET.get('query', None)
        query_text = request.GET.get('text', None)
        if query_id and query_text:
            query = YqlQuery.objects.get(id=query_id)
#            search_obj = YqlSearch()
#            search_obj.init_options()
#            context_vars['result'] = search_obj.fetch(query.query % (query.table.name, query_text))
    return direct_to_template(request, template="yql/queries.html", extra_context=context_vars)