from django.db import models

class account (models.Model):
    name = models.CharField(max_length=200)
    pin_code = models.IntegerField(default=0)
    money = models.IntegerField(default=2000)

    def __str__(self):
        return self.name


class user (models.Model):
    password = models.CharField(max_length=200)


# Create your models here.
