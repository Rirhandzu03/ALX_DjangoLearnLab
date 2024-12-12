from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/',  FeedView.as_view(), name='feed'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('unlike/<int:post_id>/', views.unlike_post, name='unlike_post'),
]