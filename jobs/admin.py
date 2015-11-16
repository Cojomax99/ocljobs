from django.contrib import admin

from jobs.models import JobsEntry, JobsQuery


class QueryAdmin(admin.ModelAdmin):
    pass


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(JobsEntry, EntryAdmin)
admin.site.register(JobsQuery, QueryAdmin)
