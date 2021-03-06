from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Status(models.Model):
    #id is automatic
    text = models.CharField(max_length=141)
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)
    #makemigrations in terminal will adjust any models that have been updated

class Favorite(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    
