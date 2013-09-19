from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from events.models import  *

class EventsPlugin(CMSPluginBase):
    model = EventPlugin
    name = "Recent_Posts"
    render_template = "pages/recent_post.html"
    
    def render(self, context, instance, placeholder):
        latest = HR_events.objects.order_by('-event_date')[:2]
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(EventsPlugin)