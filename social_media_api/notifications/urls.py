from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_notifications, name='fetch_notifications'),
]
