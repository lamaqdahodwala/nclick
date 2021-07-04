from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    points = models.IntegerField(default=0)
    cps = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
