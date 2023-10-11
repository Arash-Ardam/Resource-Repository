"""
Definition of models.
"""

import email
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class RepoData(models.Model):
    title = models.CharField(max_length=25)
    descriptions = models.CharField(max_length=200)
    dataFile = models.FileField(upload_to='app/files')
    def __str__(self):
        return self.title
    

    



