from cms.models.pluginmodel import CMSPlugin
from django.db import models
from curses.ascii import NUL

# Create your models here.
class Downloads(models.Model):
    #download file
    file = models.FileField(upload_to='downloads')
    
    #a file title 
    file_title = models.CharField(max_length=200)
    
    #a download category
    DOWNLOAD_CAT = (
        ('Supportive supervision resources', 'Supportive supervision resources'),
        ('Training manuals and Documentations', 'Training manuals and Documentations'),
        ('HRHIS Tools and Resources', 'HRHIS Tools and Resources'),
    )
    category = models.CharField(max_length=50,
                                      choices=DOWNLOAD_CAT,
                                      default='Supportive supervision resources')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.file_title

class DownloadPlugin(CMSPlugin):
    title = models.CharField(max_length=200,default='my downloads')
    