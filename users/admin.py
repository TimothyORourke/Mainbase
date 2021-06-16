from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Profile

# Register your models here.

@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    # readonly_fields = ('id', 'date_posted', 'last_updated',)
