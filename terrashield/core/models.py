from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fitness_goal = models.CharField(max_length=100, blank=True, null=True)
    available_equipment = models.TextField(blank=True, null=True)  # Store as a comma-separated string

    def __str__(self):
        return self.user.username
    
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    equipment_required = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    muscle_group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Workout Plan for {self.user.username} on {self.date_created.strftime('%Y-%m-%d')}"