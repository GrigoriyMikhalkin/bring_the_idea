from django import template
from simple_rate.models import Rating
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag
def get_rating(instance):
    content_type = ContentType.objects.get_for_model(instance)
    object_id = instance.id

    try:
        rating_obj = Rating.objects.get(content_type=content_type,object_id=object_id)
    except Rating.DoesNotExist:
        rating_obj = Rating.objects.create(content_type=content_type,object_id=object_id)

    rating = rating_obj.rating
    return rating
