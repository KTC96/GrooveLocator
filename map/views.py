from django.shortcuts import render
from django.views import generic
from .models import Event
from django.shortcuts import render
import requests


class EventList(generic.ListView):
    model = Post
