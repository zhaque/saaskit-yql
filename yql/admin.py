from django.contrib import admin
from yql.models import YqlTable, YqlQuery

class YqlQueryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(YqlQuery, YqlQueryAdmin)
admin.site.register(YqlTable)
