from django.db import models

from datetime import datetime #this will give the current date  and time 
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100000)
    created_at=models.DateTimeField(default=datetime.now,blank=True)

