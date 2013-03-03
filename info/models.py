from django.db import models

class Barista(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="baristas/", null=True, blank=True)
    bio = models.TextField()
    
    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.date_added, self.title)

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
    description = models.TextField(blank=True)
    price = models.DecimalField(blank=True)
    image = models.ImageField(upload_to="items/", null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)