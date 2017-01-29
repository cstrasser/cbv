from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


# Create your models here.
STATUS_CHOICES = [('in','In'),('out','Out'),('archived','Archived'),]


class Author(models.Model):
    name            = models.CharField(max_length = 50, default='unknown')
    date_created    = models.DateTimeField(auto_now_add = True)
      
    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name_plural = 'Authors'

class Book(models.Model):
    title           = models.CharField(max_length = 25)
    slug            = models.SlugField(max_length = 25, null = True, blank = True)
    date_created    = models.DateField(auto_now_add = True)
    status          = models.CharField(max_length = 20, choices =STATUS_CHOICES, default = 'in')
    createdBy       = models.ForeignKey(User, null = True)
    author          = models.ForeignKey(Author, blank =True)
    notes           = models.TextField( null= True, blank = True)
    
    class Meta:
        verbose_name_plural = 'Books'
        
    def __str__(self):
        return (self.title)
    
    
    
    
    
    

    
