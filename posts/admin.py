from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Post

# Register your models here.

@register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'date_posted', 'last_updated',)
