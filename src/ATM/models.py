from django.db import models
from djgentelella.settings import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

    class Meta:
        permissions = [('can_manage_client', 'Can manage clients')]

class Account (models.Model):
    name = models.CharField(max_length=200)
    pin_code = models.IntegerField(default=0)
    money = models.IntegerField(default=2000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

# Create your models here.
