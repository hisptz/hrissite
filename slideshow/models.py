from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.
class Slideshow(models.Model):
    image = models.ImageField(upload_to='carousel')
    desc_title = models.CharField(max_length=200,default='')
    desc_text = models.CharField(max_length=500,default='')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.desc_title

class SlideshowPlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='my slide show')
    