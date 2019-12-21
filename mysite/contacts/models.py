from django.db import models
from django.utils import timezone


class Contact(models.Model):
    prop = models.CharField(max_length=200, verbose_name="property")
    property_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
