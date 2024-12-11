from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions  import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from django.shortcuts import render

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
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    user = request.user
    following = user.following.all()
    posts = Post.objects.filter(author__in=following).order_by('-created_at')
    serialized_posts = [
        {
        'id': Post.id,
        'author': Post.author.username,
        'content': Post.content,
        'created_at': Post.created_at,

        }
      
    ]
    return Response(serialized_posts)