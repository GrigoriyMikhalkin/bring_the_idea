from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Rating(models.Model):
    rating = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class UserRating(models.Model):
    user = models.ForeignKey(User)
    rating = models.ForeignKey(Rating)
    rate = models.NullBooleanField(default=None)

