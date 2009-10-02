class BaseSearch:
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

