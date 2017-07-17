from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<article_id>[0-9]+)/skip/$', views.skip, name='skip'),
    url(r'^(?P<article_id>[0-9]+)/share/$', views.share, name='share'),
]
