from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    upvotes = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    
    def __Str__(self):
        return self.name
        
class Comment(models.Model):
    comments = models.TextField()
    bug = models.ForeignKey(Bug)
    author = models.ForeignKey(User)
    
    def __Str__(self):
        return self.name