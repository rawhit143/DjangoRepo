from django.contrib import admin
from JobsApp.models import *
# Register your models here.
class IndoreJobsAdmin(admin.ModelAdmin):
    list_display=['desgn','openings','location','qual','exp','contract','contact','email']
admin.site.register(IndoreJobs,IndoreJobsAdmin)
