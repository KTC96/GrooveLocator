from django.shortcuts import get_object_or_404, reverse, render
from .models import Event, SavedEvent, EventComment
from django.views.generic import TemplateView, ListView, View
from datetime import date
from django.http import HttpResponseRedirect, JsonResponse
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class Home(TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Event.objects.filter(
            event_date__gte=date.today()
        ).order_by('-event_date')
        # Filtering events bases on date, genre and location
        selected_genre = self.request.GET.get('event_genre')
        selected_city = self.request.GET.get('event_location')
        selected_date = self.request.GET.get('event_date')

        # Additional filtering based on selected genre if provided
        if selected_genre:
            queryset = queryset.filter(event_genre=selected_genre)
        # Additional filtering based on selected date if provided
        if selected_date:
            queryset = queryset.filter(event_date=selected_date)

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Retrieve all events from the Event model
        events = Event.objects.all()
        context['events'] = events

        # Retrieve selected genre, default to an empty string
        context['selected_genre'] = self.request.GET.get('event_genre', '')

        # Retrieve all distinct genres
        context['all_genres'] = (
            Event.objects.values_list('event_genre', flat=True).distinct()
        )

        # Retrieve all distinct locations
        context['all_locations'] = (
            Event.objects.values_list('event_location', flat=True).distinct()
        )

        # Retrieve selected dat, default to an empty string
        context['selected_date'] = self.request.GET.get('event_date', '')

        # Retrieve all distinct event
        context['all_dates'] = (
            Event.objects.dates('event_date', 'day', order='DESC')
        )

        return context


class EventList(ListView):
    model = Event
    template_name = 'events_list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Event.objects.filter(
            event_date__gte=date.today()
        ).order_by('event_date')
        # Filtering events bases on date, genre and location
        selected_genre = self.request.GET.get('event_genre')
        selected_city = self.request.GET.get('event_location')
        selected_date = self.request.GET.get('event_date')
        # Additional filtering based on selected genre if provided
        if selected_genre:
            queryset = queryset.filter(event_genre=selected_genre)
        # Additional filtering based on selected city if provided
        if selected_city:
            queryset = queryset.filter(event_location=selected_city)
        # Additional filtering based on selected date if provided
        if selected_date:
            queryset = queryset.filter(event_date=selected_date)
        # Message if no events found
        if not queryset.exists():
            messages.add_message(
                self.request,
                messages.INFO,
                'No Events Found'
            )

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Retrieve selected genre, default to an empty string
        context['selected_genre'] = self.request.GET.get('event_genre', '')

        # Retrieve all distinct genres from the Event model
        context['all_genres'] = (
            Event.objects.values_list('event_genre', flat=True).distinct()
        )

        # Retrieve selected city and default to an empty string
        context['selected_city'] = self.request.GET.get('event_location', '')

        # Retrieve all distinct locations from the Event model
        context['all_locations'] = (
            Event.objects.values_list('event_location', flat=True).distinct()
        )

        # Retrieve selected date, default to an empty string
        context['selected_date'] = self.request.GET.get('event_date', '')

        # Retrieve all distinct event dates
        context['all_dates'] = (
            Event.objects.dates('event_date', 'day', order='DESC')
        )

        return context


class EventDetails(View):
    template_name = "event_details.html"

    def get(self, request, slug, *args, **kwargs):
        # Retrieve the event details based on the provided slug
        event = get_object_or_404(Event, slug=slug)

        # Retrieve additional details, saved status, and user comments
        # if the user is authenticated

        details = event.event_details
        saved = False
        user_info = None

        if request.user.is_authenticated:
            saved = event.saved.filter(id=request.user.id).exists()
            user_info = EventComment.objects.filter(
                saved_event__event=event,
                user=request.user
            ).first()

        # Retrieve all comments related to the event
        comments = EventComment.objects.filter(saved_event__event=event)

        # Render the event details page with the retrieved data
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
        # Retrieve the event details based on the provided slug
        event = get_object_or_404(Event, slug=slug)

        # Retrieve additional details, saved status, and user comments
        # if authenticated
        saved = False
        user_info = None

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # If they are check if current user has saved the event
            saved = event.saved.filter(id=request.user.id).exists()
            user_info = EventComment.objects.filter(
                saved_event__event=event,
                user=request.user
            ).first()

        # Process the comment form submission
        comment_form = CommentForm(data=request.POST, instance=user_info)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user

            # Link the comment to the saved event or create a new saved event
            comment.saved_event, _ = SavedEvent.objects.get_or_create(
                user=request.user,
                event=event
            )

            comment.save()

            # Redirect to the event details page after successful comment
            # submission
            return HttpResponseRedirect(reverse('event_details', args=[slug]))

        # Retrieve all comments related to the event
        comments = EventComment.objects.filter(saved_event__event=event)

        # Render the event details page with the retrieved data
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
        # Get the saved events for the authenticated user
        if self.request.user.is_authenticated:
            return self.request.user.saved.all()
        else:
            # If user is not authenticated, return an empty queryset
            return Event.objects.none()

    def get(self, request, *args, **kwargs):
        # Get the saved events queryset
        queryset = self.get_queryset()

        # Display a message if the user has not saved any events
        if not queryset.exists():
            messages.info(request, 'You have not saved any events yet')

        # Call the parent class's get method to handle the view
        return super().get(request, *args, **kwargs)


class SaveEvent(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        # Get the event object using the provided slug
        event = get_object_or_404(Event, slug=slug)

        # Check if the authenticated user has already saved the event
        if event.saved.filter(id=request.user.id).exists():
            # If saved, remove the user from the event's saved list
            event.saved.remove(request.user)
        else:
            # If not saved, add the user to the event's saved list
            event.saved.add(request.user)

        # Redirect to the event details page after saving or removing the event
        return HttpResponseRedirect(reverse('event_details', args=[slug]))
