from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Event, SavedEvent
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date
from django.http import HttpResponseRedirect
from django.core.serializers import serialize
from django.http import JsonResponse
import requests


class home(TemplateView):
    template_name = 'index.html'

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(event_date__gte=date.today()).order_by('-event_date')
    template_name = 'events_list.html'
    paginate_by = 10



class SavedEventList(generic.ListView):
   model = SavedEvent
   template_name = 'saved_events.html'
   paginate_by = 5

class SavedEvent(View):

    def event(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.saved_by.filter(id=request.user.id).exists():
            event.saved_by.remove(request.user)
        else:
            event.saved_by.add(request.user)

        return HttpResponseRedirect(reverse('home', args=[slug]))

