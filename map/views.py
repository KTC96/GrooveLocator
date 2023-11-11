from django.shortcuts import render
from django.views import generic
from .models import Event
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date


import requests


class home(TemplateView):
    template_name = 'index.html'

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(event_date__gte=date.today()).order_by('-event_date')
    template_name = 'events_list.html'
    paginate_by = 10
