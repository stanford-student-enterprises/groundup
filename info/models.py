from django.db import models

class Barista(models.Model):
    name = models.TextField(max_length=40)
    image = models.ImageField(upload_to="baristas/")
