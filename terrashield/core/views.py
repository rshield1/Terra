from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile, WorkoutPlan
from .utils import generate_workout_plan
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import WorkoutPlan
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):
    """
    View to handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('profile')  # Redirect to profile setup after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """
    View to handle displaying and updating the user profile.
    """
    # Retrieve or create a user profile instance for the current user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form})


@login_required
def workout_plan(request):
    """
    View to generate and display the user's workout plan.
    """
    # Retrieve the latest workout plan for the user, or generate a new one if none exists
    workout_plan = WorkoutPlan.objects.filter(user=request.user).last()
    
    if not workout_plan:
        workout_plan = generate_workout_plan(request.user)
    
    return render(request, 'workout_plan.html', {'workout_plan': workout_plan})

@login_required
def dashboard(request):
    """
    View to display the user's dashboard with their workout progress and history.
    """
    workout_plans = WorkoutPlan.objects.filter(user=request.user).order_by('-date_created')

    # Calculate progress metrics
    total_workouts = workout_plans.count()
    last_week_workouts = workout_plans.filter(date_created__gte=timezone.now() - timedelta(days=7)).count()

    context = {
        'workout_plans': workout_plans,
        'total_workouts': total_workouts,
        'last_week_workouts': last_week_workouts,
    }

    return render(request, 'dashboard.html', context)

@login_required
def complete_workout(request, plan_id):
    """
    View to mark a workout plan as completed.
    """
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id, user=request.user)
    workout_plan.completed = True
    workout_plan.save()

    messages.success(request, 'Workout marked as completed!')
    return HttpResponseRedirect(reverse('dashboard'))