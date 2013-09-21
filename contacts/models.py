from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.
class Contacts(models.Model):
	position_categories=(
	('Project Coordinator','Project Coordinator'),
	('Project Administrator','Project Administrator'),
	('System Analyst','System Analyst'),
	('System Developer','System Developer'),
	('Technical supervisor','Technical supervisor'),	
	)
	member_name=models.CharField(max_length=200)
	position=models.CharField(max_length=200, choices=position_categories , default='Project Coordinator')
	phone_number=models.CharField(max_length=15, blank=True)
	e_mail=models.EmailField(max_length=200,  blank=True)
	address=models.CharField(max_length=200,  blank=True)
	
	def __unicode__(self):   # Python 3: def __str__(self):
		return self.member_name
			
class ContactsPlugin(CMSPlugin):
	title=models.CharField(max_length=200, default='implementers')
	
