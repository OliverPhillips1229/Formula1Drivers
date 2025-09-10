from django.db import models
from django.urls import reverse

class Driver(models.Model):
    name = models.CharField(max_length=100)
    current_team = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    age = models.IntegerField()
    drive_years = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('driver-detail', kwargs={'driver_id': self.id})