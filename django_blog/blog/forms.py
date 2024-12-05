from django import forms
from .models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Creating and updating of posts
class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'content']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = self.user  
        if commit:
            instance.save()
        return instance

