from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.PopularIdeasView.as_view()),
    url(r'^new/$', views.NewIdeasView.as_view()),
    url(r'^top/$', views.TopIdeasView.as_view()),
    url(r'^idea/(?P<pk>\d+)$', views.DetailIdeaView.as_view(), name="idea-detail"),
    url(r'^info/$', views.InfoView.as_view()),
    url(r'^load/comments/$', views.load_new_comments),
]
