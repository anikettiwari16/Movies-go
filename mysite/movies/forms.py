from django import forms
from .models import Booking


seat_choice = [
        ('A1','A1'),
        ('A2','A2'),
        ('A3','A3'),
        ('A4','A4'),
        ('A5','A5'),
        ('A6','A6'),
        ('A7','A7'),
        
        ('B1','B1'),
        ('B2','B2'),
        ('B3','B3'),
        ('B4','B4'),
        ('B5','B5'),
        ('B6','B6'),
        ('B7','B7'),

        ('C1','C1'),
        ('C2','C2'),
        ('C3','C3'),
        ('C4','C4'),
        ('C5','C5'),
        ('C6','C6'),
        ('C7','C7'),

        ('D1','D1'),
        ('D2','D2'),
        ('D3','D3'),
        ('D4','D4'),
        ('D5','D5'),
        ('D6','D6'),
        ('D7','D7'),

        ('E1','E1'),
        ('E2','E2'),
        ('E3','E3'),
        ('E4','E4'),
        ('E5','E5'),
        ('E6','E6'),
        ('E7','E7'),

        ('F1','F1'),
        ('F2','F2'),
        ('F3','F3'),
        ('F4','F4'),
        ('F5','F5'),
        ('F6','F6'),
        ('F7','F7'),
    ]

class BookingForm(forms.ModelForm):
	"""
	movie = forms.ModelChoiceField(label="Movie", queryset=Booking.objects.values('movie').distinct(), empty_label="Select Movie")
	theater = forms.ModelChoiceField(label="Theater", queryset=Booking.objects.values('theater').distinct(), empty_label="Select Theater")
	"""
	seat = forms.MultipleChoiceField(label='Select Seats', choices=seat_choice, widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Booking
		fields = ['movie','theater','time','seat']