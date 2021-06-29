import django.contrib.auth.models
from django.db import models

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    cps = models.IntegerField(default=0)