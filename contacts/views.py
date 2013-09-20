from django.shortcuts import render
from contacts.models import *

def contacts(request):
	contacts = Contacts.objects.all()
	context = { 'contacts':contacts }
	return render(request, 'pages/contacts.html', context)

