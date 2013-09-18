from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    # ex: /events/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
)