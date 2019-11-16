from django.db import models
from datetime import datetime
# Create your models here.
# ok

class ProjectType(models.Model):
    project_type = models.CharField(max_length=200)
    type_summary = models.CharField(max_length=200)
    type_slug = models.CharField(max_length=200, default=1)
    
    class Meta:
        verbose_name_plural = "Project Types"
    
    def __str__(self):
        return self.project_type

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_summary = models.CharField(max_length=200)
    project_type = models.ForeignKey(ProjectType, default=1, verbose_name="Type", on_delete=models.SET_DEFAULT)
    project_slug = models.CharField(max_length=200, default=1)
    
    class Meta:
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.project_name
# Thonk        
#class BugSeverity(models.Model):

class Bug(models.Model):
    bug_title = models.CharField(max_length=150)
    bug_report = models.TextField()
    #bug_project =
    project = models.ForeignKey(Project, default=1, verbose_name="Project", on_delete=models.SET_DEFAULT)
    bug_slug = models.CharField(max_length=200, default=1) 
    bug_severity = models.CharField(max_length=1)
    bug_published = models.DateTimeField('date reported', default=datetime.now)
    
    def __str__(self):
        return self.bug_title