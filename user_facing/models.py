from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points_earned = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)
    # Add other fields as needed
