from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OAuthKey(models.Model):
    key_name = models.CharField(max_length=100)
    client_id = models.TextField()
    client_secret = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
