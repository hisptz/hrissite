from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from downloads.models import  *

class DownloadsPlugin(CMSPluginBase):
    model = DownloadPlugin
    name = "Downloads"
    render_template = "pages/downloads.html"
    
    def render(self, context, instance, placeholder):
        latest = Downloads.objects.all()
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(DownloadsPlugin)