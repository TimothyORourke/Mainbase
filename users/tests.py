from django.test import TestCase

from django.contrib.auth.models import User
from .models import Follow

# Create your tests here.

class UserTestCase(TestCase):
    
    def test_is_following(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        Follow.objects.create(follower=user1, followee=user2)

        self.assertTrue(user1.is_following(user2))

    def test_is_followed_by(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        Follow.objects.create(follower=user1, followee=user2)

        self.assertTrue(user2.is_followed_by(user1))

    def test_start_following(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        user1.start_following(user2)

        self.assertTrue(user1.is_following(user2))

    def test_stop_following(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        user1.start_following(user2)
        user1.stop_following(user2)

        self.assertFalse(user1.is_following(user2))

class FollowTestCase(TestCase):

    def test_neither_user_follows(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        self.assertFalse(user1.is_following(user2))
        self.assertFalse(user1.is_followed_by(user2))
        self.assertFalse(user2.is_following(user1))
        self.assertFalse(user2.is_followed_by(user1))

    def test_one_user_follows(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        user1.start_following(user2)

        self.assertTrue(user1.is_following(user2))
        self.assertFalse(user1.is_followed_by(user2))
        self.assertFalse(user2.is_following(user1))
        self.assertTrue(user2.is_followed_by(user1))

    def test_follow_each_other(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        user1.start_following(user2)
        user2.start_following(user1)

        self.assertTrue(user1.is_following(user2))
        self.assertTrue(user1.is_followed_by(user2))
        self.assertTrue(user2.is_following(user1))
        self.assertTrue(user2.is_followed_by(user1))
        
