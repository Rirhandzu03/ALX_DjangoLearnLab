from django import forms
from .models import Post, Comment,Tag
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
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author = self.user  
        tag_names = self.cleaned_data['tags'].split(',')
        if commit:
            instance.save()
            instance.tags.clear()  # Clear existing tags
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
                instance.tags.add(tag)
        return instance
    
# Creating Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Write a comment...'}),

        }
        labels = {
            'content': '',
        }

