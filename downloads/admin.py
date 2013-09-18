from django.contrib import admin
from downloads.models import Downloads

class DownloadsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('download category', {'fields': ['category']}),
        ('Description of file', {'fields': ['file_title']}),
        ('Upload file',               {'fields': ['file']}),
    ]


admin.site.register(Downloads,DownloadsAdmin)