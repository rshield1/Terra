from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile, WorkoutPlan
from .utils import generate_workout_plan


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