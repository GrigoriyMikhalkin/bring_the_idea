from django.shortcuts import render
from django_ajax.decorators import ajax
from simple_rate.models import Rating, UserRating
from django.contrib.contenttypes.models import ContentType
from base.models import Idea
from django.db.models import F

# if rate is True -- then vote is Up, if False -- Down
def is_rated(user, rating, rate):
    ur = UserRating.objects.get_or_create(user=user,rating=rating)
    user_rate = ur.rate
    
    if user_rate == rate:
        return True
    return False
    

@ajax
def vote_up_idea(request,oid):
    content_type = ContentType.objects.get_for_model(Idea)
    rating_obj = Rating.objects.get(content_type=content_type,object_id=oid)
    rating = rating_obj.rating
    rating_obj.rating = F("rating") + 1
    rating_obj.save()
    
    return {'result': rating + 1}

@ajax
def vote_down_idea(request,oid):
    content_type = ContentType.objects.get_for_model(Idea)
    rating_obj = Rating.objects.get(content_type=content_type,object_id=oid)
    rating = rating_obj.rating
    rating_obj.rating = F("rating") - 1
    rating_obj.save()
    
    return {'result': rating - 1}
