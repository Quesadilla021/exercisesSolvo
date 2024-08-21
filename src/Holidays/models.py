from django.db import models

class Holiday(models.Model):
    name = models.CharField(max_length=100)
    weekday = models.CharField(max_length=10)
    date = models.DateField()
    country = models.CharField(max_length=3, default='CR')

    def __str__(self):
        return self.name
