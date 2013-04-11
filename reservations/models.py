from django.db import models

class ReservationItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)

    def __unicode__(self):
        return "%s" % self.name

class Reservation(models.Model):
    item = models.ForeignKey('ReservationItem')
    quantity = models.IntegerField()
    pickup_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Reservation for %d %s by %s on %s" % (self.quantity, 
                                                    self.item, 
                                                    self.pickup_name,
                                                    self.date)

class ReservationNotificationEmail(models.Model):
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.email