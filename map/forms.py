from .models import EventComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ('hotel_details', 'transport_details')
