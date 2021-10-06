from django.db import models

class Story(models.Model):
    SIZE_CHOICES = (('Small', 50), ('Medium', 100), ('Big', 200))
    TEMPERATURE_CHOICES = (('Default', 1.0), ('Creative', 1.2), ('Very Creative', 1.5))

    example = models.TextField()
    size = models.IntegerField(choices=SIZE_CHOICES)
    temperature = models.FloatField(choices=TEMPERATURE_CHOICES)

    def __str__(self):
        return "Example: " + str(self.example) + "\nTemperature: " + str(self.temperature) + "\nSize: " + str(self.size)
