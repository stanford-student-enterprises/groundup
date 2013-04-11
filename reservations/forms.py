from django.forms import ModelForm

from reservations.models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
