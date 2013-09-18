from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from slideshow.models import  *

class SlidePlugin(CMSPluginBase):
    model = SlideshowPlugin
    name = "Slideshow Plugin"
    render_template = "pages/hello_plugin.html"
    
    def render(self, context, instance, placeholder):
        latest = Slideshow.objects.all()
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(SlidePlugin)