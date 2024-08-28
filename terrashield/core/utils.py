from .models import Exercise, WorkoutPlan, UserProfile

def generate_workout_plan(user):
    """
    Generates a workout plan for the user based on their available equipment and fitness goals.

    Parameters:
    - user (User): The user for whom the workout plan is being generated.

    Returns:
    - WorkoutPlan: The generated workout plan for the user.
    """
    # Fetch user profile and available equipment
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # If the user's profile does not exist, we can't generate a workout plan
        return None

    # Get the available equipment as a list (split by comma and strip any whitespace)
    equipment = [eq.strip() for eq in profile.available_equipment.split(',')] if profile.available_equipment else []

    # Fetch exercises that match the available equipment
    exercises = Exercise.objects.filter(equipment_required__in=equipment)

    # Create a workout plan with selected exercises
    workout_plan = WorkoutPlan.objects.create(user=user)
    workout_plan.exercises.add(*exercises)
    workout_plan.save()

    return workout_plan