from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fitness_goal = models.CharField(max_length=100)
    available_equipment = models.TextField()  # Store as comma-separated values

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    equipment_required = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    muscle_group = models.CharField(max_length=100)

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    date_created = models.DateTimeField(auto_now_add=True)