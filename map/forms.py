from .models import EventComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ('hotel_details', 'transport_details')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

       
        self.fields['hotel_details'].widget.attrs['rows'] = 3  
        self.fields['hotel_details'].widget.attrs['cols'] = 40  
        self.fields['transport_details'].widget.attrs['rows'] = 3
        self.fields['transport_details'].widget.attrs['cols'] = 40
