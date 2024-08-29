from django.core.management.base import BaseCommand
from core.models import Exercise

class Command(BaseCommand):
    help = 'Populates the Exercise model with initial data.'

    def handle(self, *args, **kwargs):
        exercises = [
            {"name": "Push Up", "equipment_required": "None", "description": "A bodyweight exercise targeting chest and triceps.", "difficulty": "Medium", "muscle_group": "Chest, Triceps"},
            {"name": "Dumbbell Curl", "equipment_required": "Dumbbells", "description": "An exercise for biceps using dumbbells.", "difficulty": "Easy", "muscle_group": "Biceps"},
            {"name": "Treadmill Run", "equipment_required": "Treadmill", "description": "A cardio exercise using a treadmill.", "difficulty": "Medium", "muscle_group": "Cardio"},
            {"name": "Squat", "equipment_required": "None", "description": "A bodyweight exercise targeting the lower body.", "difficulty": "Medium", "muscle_group": "Legs"},
            {"name": "Bench Press", "equipment_required": "Barbell, Bench", "description": "A compound exercise targeting the chest.", "difficulty": "Hard", "muscle_group": "Chest, Shoulders, Triceps"},
            {"name": "Pull Up", "equipment_required": "Pull-Up Bar", "description": "A bodyweight exercise for the back and biceps.", "difficulty": "Hard", "muscle_group": "Back, Biceps"},
        ]

        for exercise in exercises:
            Exercise.objects.create(**exercise)

        self.stdout.write(self.style.SUCCESS('Successfully populated the Exercise model.'))