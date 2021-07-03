from django.db import models

# Create your models here.
class Game(models.Model):
    points = models.IntegerField(default=0)
    cps = models.IntegerField(default=0)