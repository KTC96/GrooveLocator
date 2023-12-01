from django.shortcuts import get_object_or_404, reverse, render
from .models import Event, SavedEvent, EventComment
from django.views.generic import TemplateView, ListView, View
from datetime import date
from django.http import HttpResponseRedirect, JsonResponse
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin




class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()
        context['events'] = events
        return context

class EventList(ListView):
    model = Event
    queryset = Event.objects.filter(event_date__gte=date.today()).order_by('-event_date')
    template_name = 'events_list.html'
    paginate_by = 9


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SaveEvent(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)

        if event.saved.filter(id=request.user.id).exists():
            event.saved.remove(request.user)
        else:
            event.saved.add(request.user)

        return HttpResponseRedirect(reverse('event_details', args=[slug]))