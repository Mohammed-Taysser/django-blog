from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_update',)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name='comment')
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
