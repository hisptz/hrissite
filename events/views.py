# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from events.models import *

def index(request):
    latest_events_list = HR_events.objects.order_by('-event_date')[:5]
    context = {'latest_events_list': latest_events_list}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    try:
        event = HR_events.objects.get(pk=event_id)
    except HR_events.DoesNotExist:
        raise Http404
    return render(request, 'events/details.html', {'event': event})
    