from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models import F

from django_ajax.decorators import ajax

from simple_rate.models import Rating, UserRating
from base.models import Idea, Comment


# if rate is True -- then vote is Up, if False -- Down
def is_rated(user, rating, rate):
    ur = UserRating.objects.get_or_create(user=user,rating=rating)
    user_rate = ur.rate
    
    if user_rate == rate:
        return True
    return False


def rate_object(object_id, object_type, increment=True):
    content_type = ContentType.objects.get_for_model(object_type)
    rating_obj = Rating.objects.get(content_type=content_type,object_id=object_id)
    rating = rating_obj.rating

    if increment:
        rating_obj.rating = F("rating") + 1
        rating_obj.save()
        return {'result': rating + 1}
    else:
        rating_obj.rating = F("rating") - 1
        rating_obj.save()
        return {'result': rating - 1}


@ajax
def vote_up_idea(request,oid):
    return rate_object(oid, Idea)

@ajax
def vote_down_idea(request,oid):
    return rate_object(oid, Idea, increment=False)

@ajax
def vote_up_comment(request,oid):
    return rate_object(oid, Comment)

@ajax
def vote_down_comment(request,oid):
    return rate_object(oid, Comment, increment=False)
