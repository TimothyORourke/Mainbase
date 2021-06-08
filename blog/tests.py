from django.test import TestCase

import datetime

from django.utils import timezone

from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class PostTestCase(TestCase):

    def test_text(self):
        post = Post(text='test text')
        self.assertTrue(post.text == 'test text')

    def test_was_posted_today(self):
        user = User.objects.create()
        two_days_ago = timezone.now() - datetime.timedelta(days=2)
        post = Post.objects.create(author=user)
        post2 = Post.objects.create(author=user, date_posted=two_days_ago)
        self.assertTrue(post.was_posted_today())
        self.assertTrue(post2.was_posted_today())
    