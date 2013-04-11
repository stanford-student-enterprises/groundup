from django.contrib import admin

from reservations.models import Reservation, ReservationNotificationEmail, ReservationItem 

admin.site.register(Reservation)
admin.site.register(ReservationItem)
admin.site.register(ReservationNotificationEmail)