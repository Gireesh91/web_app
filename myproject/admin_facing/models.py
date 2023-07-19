from django.db import models

class AndroidApp(models.Model):
    name = models.CharField(max_length=100)
    points_earned = models.IntegerField()
