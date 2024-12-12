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
    

@login_required
def like_post(request, post_id):
    # Check if the post exists
    post = get_object_or_404(Post, id=post_id)

    # Check if the user has already liked this post
    if Like.objects.filter(user=request.user, post=post).exists():
        return JsonResponse({"message": "You have already liked this post."}, status=400)

    # Create a like object
    like = Like(user=request.user, post=post)
    like.save()

    # Create a notification
    notification = Notification(
        recipient=post.user,  
        actor=request.user,  
        verb="liked your post",
        target_content_type=ContentType.objects.get_for_model(Post),
        target_object_id=post.id,
        target=post
    )
    notification.save()

    return JsonResponse({"message": "Post liked successfully."}, status=201)

@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()

    if not like:
        return JsonResponse({"message": "You have not liked this post."}, status=400)

    # Delete the like object
    like.delete()

    return JsonResponse({"message": "Post unliked successfully."}, status=200)