from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('profile/', core_views.profile, name='profile'),
    path('workout/', core_views.workout_plan, name='workout_plan'),
    path('register/', core_views.register, name='register'),
    
    # Include Django's built-in authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]