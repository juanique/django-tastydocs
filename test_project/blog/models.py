from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    content = models.TextField(help_text="What the user has to say about the post.")
    author = models.ForeignKey(User)


class Actor(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    name = models.CharField(max_length=32)
    actors = models.ManyToManyField(Actor, related_name='movies')
