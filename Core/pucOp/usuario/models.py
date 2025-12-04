from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    