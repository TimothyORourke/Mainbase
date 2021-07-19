from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Profile, Follow

# Register your models here.

@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@register(Follow)
class FollowAdmin(admin.ModelAdmin):
    pass