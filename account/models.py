from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShortenedURL(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
    counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.original_url} - by {self.user.username}"