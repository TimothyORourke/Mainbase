from django.db import models
from django.contrib.auth.models import User

from uuid import uuid4
import datetime
from django.utils import timezone

# Create your models here.

def uuid_hex():
    return uuid4().hex

class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=32, editable=False, default=uuid_hex)
    text = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def was_posted_today(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return self.text
