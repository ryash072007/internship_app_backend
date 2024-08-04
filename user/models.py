from django.db import models

# Create your models here.

class UserData(models.Model):
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Username