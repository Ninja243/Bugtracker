from django.contrib import admin
from .models import Bug, Project, ProjectType
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
# ok
class BugAdmin(admin.ModelAdmin):
    #fields = ["bug_title", "bug_report", "bug_published", "bug_severity"]
    fieldsets = [
        ("Overview", {'fields':["bug_title", "bug_severity", "bug_slug"] }),
        ("Report", {"fields":["bug_published", "project", "bug_report"]})
        
    ]
    
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()},
    }
admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(Bug,BugAdmin)
