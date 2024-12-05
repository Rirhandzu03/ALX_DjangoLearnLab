from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import post

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

# Implementing CRUD Operations
class postListView(ListView):
    model = post
    template_name = 'blog/post_list.html'
    context_object_name = 'post'

class PostDetailView(DetailView):
    model = post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(DetailView):
    model = post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')   

    def get_queryset(self):
        return post.objects.filter(author=self.request.user) 

class PostDeleteView(DetailView):
    model = post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


    def get_queryset(self):
        return post.objects.filter(author=self.request.user)

    




            


