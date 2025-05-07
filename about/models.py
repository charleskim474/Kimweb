from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length = 20)
    tel = models.CharField(max_length = 20)
    email = models.EmailField(null = True)
    idea = models.TextField()
    budget = models.IntegerField()