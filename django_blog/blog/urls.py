from django.urls import path
from . import views
from .views import register, CustomLoginView, CustomLogoutView, profile, PostByTagListView 
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [  
    
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Defining urls for CRUD operations
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    #path('posts/<int:post_id>/', views.PostDetailView, name='post_detail'),
    # Add Comment URLs
    #path('comment/<int:pk>/update/', 'post/<int:pk>/comments/new/'),
    path('comment/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    path('search/', views.search, name='search'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='tag_posts'),  # Correct slug URL pattern
    path('tags/<str:tag_name>/', views.tag_posts, name='tag_posts'),
    # other paths
]


