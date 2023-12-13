from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Event(models.Model):
    title = models.CharField(max_length=250, unique=True, default="event")
    slug = models.SlugField(max_length=200, unique=True)
    event_genre = models.CharField(max_length=50)
    event_price = models.DecimalField(max_digits=10, decimal_places=2)
    event_location = models.CharField(max_length=250)
    event_venue = models.CharField(max_length=200, null=True)
    event_date = models.DateField(default=timezone.now)
    event_time = models.TimeField(null=True)
    event_details = models.TextField()
    saved = models.ManyToManyField(
        User,
        related_name="saved",
        blank=True,
        default=False
    )
    image = CloudinaryField('image', default='placeholder')
    latitude = models.FloatField(max_length=200, null=True)
    longitude = models.FloatField(max_length=200, null=True)

    def __str__(self):
        return self.title

    def number_saved_event(self):
        return self.saved.count()


class SavedEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='saved_events'
    )

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"


class EventComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_event = models.ForeignKey(SavedEvent, on_delete=models.CASCADE)
    comment_text = models.TextField()
    hotel_details = models.TextField(max_length=150, blank=True, null=True)
    transport_details = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
