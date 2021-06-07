from django.contrib import admin
from django.contrib.admin.decorators import register

from . import models

# Register your models here.

@register(models.Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'last_updated',)
