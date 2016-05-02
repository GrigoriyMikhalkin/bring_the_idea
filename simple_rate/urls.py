from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^idea/up/(?P<oid>\d+)$', vote_up_idea),
    url(r'^idea/down/(?P<oid>\d+)$', vote_down_idea),
    url(r'^comment/up/(?P<oid>\d+)$', vote_up_comment),
    url(r'^comment/down/(?P<oid>\d+)$', vote_down_comment),
]
