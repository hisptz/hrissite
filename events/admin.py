from django.contrib import admin
from events.models import *

class ChoiceInline(admin.TabularInline):
    model = Event_photos
    extra = 4

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Title',               {'fields': ['event_name']}),
        ('Short Discription Of Event', {'fields': ['event_discription']}),
        ('Event Date', {'fields': ['event_date']}),
    ]
    inlines = [ChoiceInline]
    
    list_display = ('event_name','event_date','event_discription')
    list_filter = ['event_date']
    search_fields = ['desc_title']
admin.site.register(HR_events,EventAdmin)