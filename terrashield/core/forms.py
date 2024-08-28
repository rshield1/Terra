from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fitness_goal', 'available_equipment']
        widgets = {
            'available_equipment': forms.TextInput(attrs={'placeholder': 'e.g., dumbbells, treadmill'}),
        }