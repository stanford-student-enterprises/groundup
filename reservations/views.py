from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

from reservations.forms import ReservationForm
from reservations.models import  ReservationNotificationEmail

def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            emails = [rne.email for rne in ReservationNotificationEmail.objects.all()]
            send_mail("New Groundup Reservation",
                    "Item: %s \n Name: %s \n Quantity: %d" % (reservation.item, reservation.pickup_name, reservation.quantity),
                    "groundup.website@gmail.com",
                    emails)
            return render_to_response('reservations/complete.html', {'reservation': reservation})
    else:
        form = ReservationForm()

    return render_to_response('reservations/reserve.html', {'form': form},
                            context_instance=RequestContext(request))
