from django.db import models
from django.urls import reverse

SESSIONS = (
    ('Q', 'Qualifying'),
    ('S', 'Sprint'),
    ('R', 'Race'),
)

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


class Result(models.Model):
    date = models.DateField('Race date')
    session = models.CharField(
        max_length=1,
        choices=SESSIONS,
        default=SESSIONS[2][0]  # default to 'R' (Race)
    )
    position = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_session_display()} • P{self.position} on {self.date}"

    class Meta:
        ordering = ['-date']
        
class Helmet(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='helmets/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('helmet-index')