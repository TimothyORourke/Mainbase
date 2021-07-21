from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

# Creates a profile for a newly created User
@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)
    profile_banner = models.ImageField(null=True, blank=True)
    bio = models.TextField(blank=True, max_length=280)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followee")
    date_followed = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.follower.username} follows {self.followee.username}"

class UserFunctions():

    def is_following(self, user):
        return len(self.follower.filter(followee=user)) > 0

    def is_followed_by(self, user):
        return len(self.followee.filter(follower=user)) > 0

    def start_following(self, user):
        Follow.objects.create(follower=self, followee=user)

    def stop_following(self, user):
        if (self.is_following(user)):
            Follow.objects.get(follower=self, followee=user).delete()

User.__bases__ += (UserFunctions,)