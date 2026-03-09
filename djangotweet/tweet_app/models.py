from django.db import models

# Create your models here.

class Tweet(models.Model):
    username = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tweet nick: {self.username} message: {self.message} Tweet time: {self.created_at}"