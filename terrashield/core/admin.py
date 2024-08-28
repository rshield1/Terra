from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
from .models import Exercise, WorkoutPlan

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)