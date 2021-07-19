from django.test import TestCase

from django.contrib.auth.models import User
from .models import Follow

# Create your tests here.

class FollowTestCase(TestCase):

    def test_neither_user_follows(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        queryset1 = Follow.objects.filter(user=user1)
        queryset2 = Follow.objects.filter(user=user2)

        self.assertTrue(len(queryset1) == 0)
        self.assertTrue(len(queryset2) == 0)

    def test_one_user_follows(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        Follow.objects.create(user=user1, follows=user2)

        self.assertTrue(user1.following.all()[0].follows == user2)
        self.assertTrue(len(user1.followers.all()) == 0)
        self.assertTrue(len(user2.following.all()) == 0)
        self.assertTrue(user2.followers.all()[0].user == user1)

    def test_follow_each_other(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")

        Follow.objects.create(user=user1, follows=user2)
        Follow.objects.create(user=user2, follows=user1)

        self.assertTrue(user1.following.all()[0].follows == user2)
        self.assertTrue(user1.followers.all()[0].user == user2)
        self.assertTrue(user2.following.all()[0].follows == user1)
        self.assertTrue(user2.followers.all()[0].user == user1)
        
