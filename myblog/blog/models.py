from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=35,default='Title')
    content=models.TextField(null=True,blank=True)