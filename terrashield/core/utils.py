from .models import Exercise, WorkoutPlan, UserProfile

def generate_workout_plan(user):
    """
    Generates a workout plan for the user based on their available equipment, fitness goals, and difficulty levels.

    Parameters:
    - user (User): The user for whom the workout plan is being generated.

    Returns:
    - WorkoutPlan: The generated workout plan for the user.
    """
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return None

    equipment = [eq.strip() for eq in profile.available_equipment.split(',')] if profile.available_equipment else []
    fitness_goal = profile.fitness_goal.lower() if profile.fitness_goal else "general"

    # Adjust exercise selection based on fitness goal
    if fitness_goal == "weight loss":
        exercises = Exercise.objects.filter(equipment_required__in=equipment, muscle_group__in=["Cardio", "Legs"])
    elif fitness_goal == "muscle gain":
        exercises = Exercise.objects.filter(equipment_required__in=equipment, difficulty__in=["Medium", "Hard"], muscle_group__in=["Chest", "Back", "Legs", "Arms"])
    else:  # General fitness or no specific goal
        exercises = Exercise.objects.filter(equipment_required__in=equipment)

    workout_plan = WorkoutPlan.objects.create(user=user)
    workout_plan.exercises.add(*exercises)
    workout_plan.save()

    return workout_plan