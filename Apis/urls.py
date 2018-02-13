from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from reporter import settings
from Discussion.views import *
from rest_framework.authtoken import views as tokenView

urlpatterns = patterns('',
    url(r'^login/', tokenView.obtain_auth_token),
    # url(r'^list/', discussions_list, name = 'discussions_list'),
    url(r'^discussion/list/$',discussions_list.as_view()),
    # url(r'^create/', comment_create,name = 'comment_create'),
    url(r'^comment/add/$',comment_create.as_view()),
    # url(r'^discussion/list/', discussions_Searchlist, name = 'discussions_Searchlist'),
    url(r'^discussion/details/$', discussions_Searchlist.as_view()),
)