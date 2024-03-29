from django.db import models

class Mobile(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    RAM = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    audiojack = models.BooleanField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)

