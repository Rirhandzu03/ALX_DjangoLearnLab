from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class FollowTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='password')
        self.user2 = get_user_model().objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')

    def test_follow_user(self):
        response = self.client.post(f'/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user2, self.user1.following.all())

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        response = self.client.post(f'/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.user2, self.user1.following.all())