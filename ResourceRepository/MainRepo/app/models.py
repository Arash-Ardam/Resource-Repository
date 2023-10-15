"""
Definition of models.
"""

import email
from pickle import TRUE
from pyexpat import model
from django.conf import settings
from django.db import models

# Create your models here.

class RepoData(models.Model):
    title = models.CharField(max_length=25)
    descriptions = models.CharField(max_length=200)
    dataFile = models.FileField(blank=True,null=True,upload_to='files/%Y/%m')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
    

    



