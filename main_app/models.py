from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    current_team = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    age = models.IntegerField()
    drive_years = models.CharField(max_length=100)

    def __str__(self):
        return self.name