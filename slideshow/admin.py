from django.contrib import admin
from slideshow.models import Slideshow

class SlideshowAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['image']}),
        ('Image Title', {'fields': ['desc_title']}),
        ('Image description', {'fields': ['desc_text']}),
    ]
    
    list_display = ('desc_title','image','desc_text')
    #list_filter = ['pub_date']
    search_fields = ['desc_title']


admin.site.register(Slideshow,SlideshowAdmin)