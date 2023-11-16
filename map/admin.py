from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('event_date', 'event_location')
    list_display = ('title','event_date', 'event_location')
    search_fields = ('title','event_location')
    summernote_fields = ('event_details')

    
    
