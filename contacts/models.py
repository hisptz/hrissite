from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.
class Contacts(models.Model):
	member_name=models.CharField(max_length=200)
	position=models.CharField(max_length=200)
	phone_number=models.CharField(max_length=15, default='+255')
	e_mail=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	
	def __unicode__(self):   # Python 3: def __str__(self):
		return self.name
			
class ContactsPlugin(CMSPlugin):
	title=models.CharField(max_length=200, default='contacts')
	
