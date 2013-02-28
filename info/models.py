from django.db import models

class Barista(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="baristas/", null=True, blank=True)
    bio = models.TextField()
    
    def __unicode__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="vendors/", null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name
        
class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('F', "Food"),
        ('D', "Drinks"),
        ('O', "Other"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)
    image = models.ImageField(upload_to="items/", null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __unicode__(self):
    	return self.name