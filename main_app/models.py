from django.db import models
from django.urls import reverse

SESSIONS = (
    ('Q', 'Qualifying'),
    ('S', 'Sprint'),
    ('R', 'Race'),
)

class Helmet(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='helmets/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('helmet-index', kwargs={'pk: self.id'})

class Driver(models.Model):
    name = models.CharField(max_length=100)
    current_team = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    age = models.IntegerField()
    drive_years = models.CharField(max_length=100)
    helmets = models.ManyToManyField(Helmet, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('driver-detail', kwargs={'driver_id': self.id})



class Track(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    length_km = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.country})"

class Result(models.Model):
    date = models.DateField('Race date')
    session = models.CharField(
        max_length=1,
        choices=SESSIONS,
        default=SESSIONS[2][0]  # default to 'R' (Race)
    )
    position = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.get_session_display()} • P{self.position} on {self.date}"

    class Meta:
        ordering = ['-date']
        
