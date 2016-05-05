from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from ckeditor.fields import RichTextField
from simple_rate.models import Rating

from .fields import SkypeField, TelegramField


class Idea(models.Model):
    title = models.CharField(max_length=128)
    content = RichTextField()
    source = models.URLField(null=True)
    email = models.EmailField(null=True)
    skype = SkypeField(null=True)
    telegram = TelegramField(null=True)
    author = models.CharField(max_length=32,default="anon")
    displayed = models.PositiveIntegerField(default=0)
    rating = GenericRelation(Rating)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    idea = models.ForeignKey(Idea, related_name="comments")
    position = models.PositiveIntegerField(default=0)
    content = models.TextField()
    #reply_to = models.ForeignKey("Comment", related_name="replies", null=True)
    author = models.CharField(max_length=32,default="anon")
    rating = GenericRelation(Rating)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replies")
    reply = models.ForeignKey(Comment, related_name="mentions")
