from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.text
