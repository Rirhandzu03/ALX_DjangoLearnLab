from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name ='blog/logout.html'

# View for profile management
@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html')


            


