from django.db import models

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

