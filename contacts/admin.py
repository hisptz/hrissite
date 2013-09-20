from django.contrib import admin
from contacts.models import *
class MembersAdmin(admin.ModelAdmin):
	fieldsets=[
	('Name', {'fields':['member_name']}),
	('Position in project', {'fields':['position']}),
	('Institution / company', {'fields':['address']}),
	('E-mail', {'fields':['e_mail']}),
	('Phone Number', {'fields':['phone_number']}),	
	]
	list_display=('member_name','position','address','e_mail','phone_number',)
	search_fields = ['member_name']
admin.site.register(Contacts,MembersAdmin)
