from django.contrib import admin
from project.models import Project, Report


class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )


# Register your models here.
admin.site.register(Project)
admin.site.register(Report)
