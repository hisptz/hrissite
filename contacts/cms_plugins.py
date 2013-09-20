from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from contacts.models import  *

class ContactsPlugin(CMSPluginBase):
	model = ContactsPlugin
	name = 'implemeters'
	render_template = 'pages/implementers.html'
	def render(self, context, instance, placeholder):
		contacts=Contacts.objects.all()
		context.update({
		'instance': instance,
		'placeholder':placeholder,
		'contacts':contacts,		
		})
		return context

	
plugin_pool.register_plugin(ContactsPlugin)		
