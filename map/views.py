from django.shortcuts import get_object_or_404, reverse, render
from .models import Event, SavedEvent, EventComment
from django.views.generic import TemplateView, ListView, View
from datetime import date
from django.http import HttpResponseRedirect, JsonResponse
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages





class home(TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Event.objects.filter(event_date__gte=date.today()).order_by('-event_date')
        selected_genre = self.request.GET.get('event_genre')
        selected_city = self.request.GET.get('event_location')
        selected_date = self.request.GET.get('event_date')

        # Additional filtering based on selected genre if provided
        if selected_genre:
            queryset = queryset.filter(event_genre=selected_genre)

        if selected_date:
            queryset = queryset.filter(event_date=selected_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()
        context['events'] = events
        context['selected_genre'] = self.request.GET.get('event_genre', '')  
        context['all_genres'] = Event.objects.values_list('event_genre', flat=True).distinct()  
        context['all_locations'] = Event.objects.values_list('event_location', flat=True).distinct()   
        context['selected_date'] = self.request.GET.get('event_date', '')
        context['all_dates'] = Event.objects.dates('event_date', 'day', order='DESC')

        return context

class EventList(ListView):
    model = Event
    template_name = 'events_list.html'
    paginate_by = 9
   
    def get_queryset(self):
        queryset = Event.objects.filter(event_date__gte=date.today()).order_by('-event_date')
        selected_genre = self.request.GET.get('event_genre')
        selected_city = self.request.GET.get('event_location')
        selected_date = self.request.GET.get('event_date')

       
        if selected_genre:
            queryset = queryset.filter(event_genre=selected_genre)

        if selected_city:
            queryset = queryset.filter(event_location=selected_city)
        
        if selected_date:
            queryset = queryset.filter(event_date=selected_date)

        if not queryset.exists():
            messages.add_message(self.request, messages.INFO, 'No Events Found')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_genre'] = self.request.GET.get('event_genre', '')  
        context['all_genres'] = Event.objects.values_list('event_genre', flat=True).distinct()  
        context['selected_city'] = self.request.GET.get('event_location', '')
        context['all_locations'] = Event.objects.values_list('event_location', flat=True).distinct()
        context['selected_date'] = self.request.GET.get('event_date', '')
        context['all_dates'] = Event.objects.dates('event_date', 'day', order='DESC')

        return context

class EventDetails(View):
    template_name = "event_details.html"

    def get(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        details = event.event_details
        saved = False
        user_info = None

        if request.user.is_authenticated:
            saved = event.saved.filter(id=request.user.id).exists()
            user_info = EventComment.objects.filter(saved_event__event=event, user=request.user).first()

        comments = EventComment.objects.filter(saved_event__event=event)

        return render(
            request,
            self.template_name,
            {
                "event": event,
                "event_details": details,
                "saved": saved,
                "comment_form": CommentForm(instance=user_info),
                "comments": comments,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        saved = False
        user_info = None

        if request.user.is_authenticated:
            saved = event.saved.filter(id=request.user.id).exists()
            user_info = EventComment.objects.filter(saved_event__event=event, user=request.user).first()

        comment_form = CommentForm(data=request.POST, instance=user_info)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.saved_event, _ = SavedEvent.objects.get_or_create(user=request.user, event=event)
            comment.save()

            return HttpResponseRedirect(reverse('event_details', args=[slug]))

        comments = EventComment.objects.filter(saved_event__event=event)

        return render(
            request,
            self.template_name,
            {
                "event": event,
                "event_details": event.event_details,
                "saved": saved,
                "comment_form": comment_form,
                "comments": comments, 
            },
        )

class SavedEventList(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'saved_events.html'
    paginate_by = 9

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user.saved.all()
        else:
            return Event.objects.none()
    
class SaveEvent(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)

        if event.saved.filter(id=request.user.id).exists():
            event.saved.remove(request.user)
        else:
            event.saved.add(request.user)

        return HttpResponseRedirect(reverse('event_details', args=[slug]))