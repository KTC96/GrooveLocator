from django.db import models
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_id = models.CharField(max_length=200, unique=True)
    event_name = models.CharField(max_length=300)
    event_genre = models.CharField(max_length=50)
    event_price = models.DecimalField(max_digits=10, decimal_places=2)
    event_location = models.CharField(max_length=250)
    saved_by = models.ManyToManyField(User, related_name="event_saved", blank=True)

    def __str__(self):
        return self.title
    
    def number_saved_event(self):
        return self.saved.count()

class SavedEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"


class Calendar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_events = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Calendar"


class EventComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_event = models.ForeignKey(SavedEvent, on_delete=models.CASCADE)
    comment_text = models.TextField()
    hotel_details = models.TextField(blank=True, null=True)
    transport_details = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

