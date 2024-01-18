from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import TodoItem

UserModel = get_user_model()

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model  = UserModel
        fields = ["username","password1","password2"]
        
class TodoForm(forms.ModelForm):
    
    class Meta:
        fields = "__all__"
        