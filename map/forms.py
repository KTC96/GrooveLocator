from .models import EventComment
from django import forms

class CommentForm(forms.ModelForm):
    # Form for handling comments on a saved event

    class Meta:
        model = EventComment
        fields = ('hotel_details', 'transport_details')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        # Customize the appearance of the hotel_details field in the form
        self.fields['hotel_details'].widget.attrs['rows'] = 3
        self.fields['hotel_details'].widget.attrs['cols'] = 40
        self.fields['hotel_details'].widget.attrs['placeholder'] = (
            'Your hotel details will be securely stored here upon saving.'
        )

        # Customize the appearance of the transport_details field in the form
        self.fields['transport_details'].widget.attrs['rows'] = 3
        self.fields['transport_details'].widget.attrs['cols'] = 40
        self.fields['transport_details'].widget.attrs['placeholder'] = (
            'Your transport details will be securely stored here upon saving.'
        )
