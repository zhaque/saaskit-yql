from django.db import models
#import django_pipes as pipes

#class BaseSearch(pipes.Pipe):
#    uri = ''
#    cache_expiry = 3000000000
#
#    def init_options(self):
#        self.options = dict()
#
#    def set_query(self, query):
#        pass
#
#    def set_format(self, format):
#        pass
#
#    def set_callback(self, callback):
#        pass
#
#    def set_env(self, env):
#        pass
#
#    def get_result(self, response):
#        pass
#
#    def fetch(self, query, format=None, callback=None):
#        self.set_query(query)
#        if format:
#            self.set_format(format)
#        if callback:
#            self.set_callback(callback)
#
#        response = self.fetch_with_options(self.options)
#        return self.get_result(response)
#
#    def fetch_with_options(self, options):
#        resp = self.objects.get(options)
#        if resp:
#            return resp
#        return None
#
#class YqlSearch(BaseSearch):
#    uri = "http://query.yahooapis.com/v1/public/yql"
#
#    def init_options(self):
#        super(YqlSearch, self).init_options()
#        self.set_format()
#        self.set_env()
#
#    def set_query(self, query):
#        self.options.update({'q':query})
#
#    def set_format(self, format='json'):
#        self.options.update({'format':format})
#
#    def set_callback(self, callback):
#        self.options.update({'callback':callback})
#
#    def set_env(self, env='http://datatables.org/alltables.env'):
#        self.options.update({'env':env})
#
#    def get_result(self, response):
#        if response and hasattr(response, "query"):
#            response = response.query
#        elif response and hasattr(response, "error"):
#            response = response.error
#        else:
#            return None
#
#        return response

class YqlTable(models.Model):
    name = models.CharField(max_length=255)
    oauth = models.BooleanField()

    def __unicode__(self):
        return self.name    

class YqlQuery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    query = models.CharField(max_length=255)
    table = models.ForeignKey(YqlTable, verbose_name="yql table")

    def __unicode__(self):
        return '%s for %s' % (self.name, self.table)

class YqlParam(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    table = models.ForeignKey(YqlTable, verbose_name="yql table", related_name='params')

    def __unicode__(self):
        return '%s = %s for %s' % (self.name, self.value, self.table)

