from django.db import models
from django.utils import timezone


class Realtor(models.Model):
    name = models.CharField(max_length=40)
    photo = models.FileField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name