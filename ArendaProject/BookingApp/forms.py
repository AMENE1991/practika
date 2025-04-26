from django import forms
from BookingApp.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_days', 'num_guests']