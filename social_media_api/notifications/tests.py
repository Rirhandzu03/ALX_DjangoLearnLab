from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification
from posts.models import Post

# Create your tests here.
class NotificationTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(user=self.user1, title='Test Post', content='Test Content')

    def test_notification_on_like(self):
        Notification.objects.create(recipient=self.user1, actor=self.user2, verb='liked your post', target=self.post)
        notifications = Notification.objects.filter(recipient=self.user1)
        self.assertEqual(notifications.count(), 1)



