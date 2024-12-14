from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions  import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update','destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
           return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# Feed generation
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        following_users = request.user.following.all() 
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Handle like logic
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({'message': 'Post liked successfully.'}, status=201)

        return Response({'message': 'Post already liked.'}, status=400)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        # Use generics.get_object_or_404 to retrieve the post
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Handle unlike logic
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({'message': 'Post unliked successfully.'}, status=200)