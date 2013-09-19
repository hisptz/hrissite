from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.
class HR_events(models.Model): 
    event_name = models.CharField(max_length=200)
    event_discription = models.TextField(max_length=5000)
    event_date = models.DateField('date of event')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.event_name
    
class Event_photos(models.Model):
    event = models.ForeignKey('HR_events',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events')
    title = models.CharField(max_length=200,null=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    
class EventPlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='recent posts')