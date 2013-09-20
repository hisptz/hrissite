from django.conf.urls import patterns, url

from contacts import views

urlpatterns = patterns('',
     url(r'^$', views.contacts, name='contacts'),
    
)
