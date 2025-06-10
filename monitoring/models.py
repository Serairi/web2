from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    energy = models.FloatField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.station.name} - {self.timestamp}"
