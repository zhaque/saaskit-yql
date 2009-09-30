from django.contrib import admin
from yql.models import YqlTable, YqlQuery, YqlParam

class ParamsInline(admin.TabularInline):
    model = YqlParam

class YqlTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'oauth',)
    inlines = [ParamsInline,]

class YqlQueryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('table',)

class YqlParamAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'table',)
    list_filter = ('table', 'name',)

admin.site.register(YqlQuery, YqlQueryAdmin)
admin.site.register(YqlTable, YqlTableAdmin)
admin.site.register(YqlParam, YqlParamAdmin)
