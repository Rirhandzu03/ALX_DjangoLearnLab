from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like
from django.test import TestCase

# Create your tests here.
class LikeTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(user=self.user1, title='Test Post', content='Test Content')

    def test_like_post(self):
        self.client.login(username='user2', password='pass')
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Like.objects.filter(user=self.user2, post=self.post).exists())