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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)
    profile_banner = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=280)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    date_followed = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} follows {self.follows.username}"

