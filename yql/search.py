class BaseSearch(object):
    # override it for custom fetch
    def raw_fetch(self, query, *args, **kwargs):
        pass

    # override it for custom result parsing 
    def get_result(self, response):
        pass

    # public method, don't override it in child classes, do it with raw_fetch instead
    def fetch(self, query, *args, **kwargs):
        response = self.raw_fetch(query, *args, **kwargs)
        return self.get_result(response)

import settings
import yahoo.yql
import yahoo.application
class YqlSearch(BaseSearch):
    def raw_fetch(self, query, oauth=False):
        if oauth:
            oauthapp = yahoo.application.OAuthApplication(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.APPLICATION_ID, settings.CALLBACK_URL)
            request_token = oauthapp.get_request_token()
            redirect_url  = oauthapp.get_authorization_url(request_token, settings.CALLBACK_URL)
            access_token  = oauthapp.get_access_token(request_token)
            oauthapp.token = access_token
            response = oauthapp.yql(query)
        else:
            response = yahoo.yql.YQLQuery().execute(query)
        return response

    def get_result(self, response):
        res = dict()
        if 'query' in response and 'results' in response['query']:
            res.update({'yql':response['query']['results']})
        elif 'error' in response:
            res.update({'errors':('YQL query failed with error: "%s".' % response['error']['description'],)})
        else:
            res.update({'errors':('YQL response malformed.',)})
        return res

class SimpleYqlSearch(YqlSearch):
    """
    SimpleYqlSearch class provides yql search using YqlSearch but using simple query string like 'django'
    set_table fucntion MUST be run before first fetch.
    """

    yql = 'select * from %s where %s=\'%s\''
    queryname = 'query'
    count = 10
    offset = 0

    def set_yql(self, yql):
        self.yql = yql

    def set_table(self, table):
        self.table = table + '(0)'

    def set_count(self, count):
        self.count = count

    def set_offset(self, offset):
        self.offset = offset

    def set_queryname(self, queryname):
        self.queryname = queryname

    def raw_fetch(self, query, oauth=False):
        yql_query = self.yql % (self.table, self.queryname, query)
        if self.count:
            yql_query += ' limit %s' % self.count
        if self.offset:
            yql_query += ' offset %s' % self.offset
        yql_query += '|sort(field="updated",descending="true")'
        return super(SimpleYqlSearch, self).raw_fetch(yql_query, oauth)


