from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amsubjects = models.TextField()
    amattendance = models.TextField()
    amtimetable = models.TextField()
    adidcount = models.IntegerField()
