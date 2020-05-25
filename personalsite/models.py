from django.db import models
from datetime import *

# Create your models here.
class About(models.Model):
    about = models.TextField(max_length=2587)

    def __str__(self):
        return ('About Updated')

class Research(models.Model):
    paperName = models.CharField(max_length=100)
    paperDescription = models.CharField(max_length=10000)
    paper = models.FileField(upload_to = 'research_papers/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.paperName

class Publication(models.Model):
    paperName = models.CharField(max_length=100)
    paperDescription = models.CharField(max_length=10000)
    paper = models.FileField(upload_to = 'research_papers/')
    date = models.DateField(auto_now=True)

