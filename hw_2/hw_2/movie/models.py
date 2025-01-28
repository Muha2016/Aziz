from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    producer = models.CharField(max_length=100)
    duration = models.IntegerField()  # Продолжительность в секундах

    def __str__(self):
        return self.title
