def generate_workout_plan(user):
    # Fetch user profile and available equipment
    profile = user.userprofile
    equipment = profile.available_equipment.split(',')
    
    # Fetch exercises that match available equipment
    exercises = Exercise.objects.filter(equipment_required__in=equipment)
    
    # Create a workout plan with selected exercises
    workout_plan = WorkoutPlan.objects.create(user=user)
    workout_plan.exercises.add(*exercises)
    workout_plan.save()
    
    return workout_plan