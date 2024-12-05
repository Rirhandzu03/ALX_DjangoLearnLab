from django.urls import path
from . import views
from .views import register, CustomLoginView, CustomLogoutView, profile

urlpatterns = [  # Corrected here

    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
