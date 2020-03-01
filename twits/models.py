from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Twit(models.Model):
    content = models.TextField(max_length=150)
    created_at = models.DateTimeField(default=timezone)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} Twit"

    @property
    def comments_count(self):
        return Comment.objects.filter(twit=self).count()


class Comment(models.Model):
    content = models.TextField(max_length=150)
    created_at = models.DateTimeField(default=timezone)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)