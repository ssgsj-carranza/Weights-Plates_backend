from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('none', 'none')
)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='none')
    # age = models.IntegerField(default=0)
    # weight = models.IntegerField(default=0)
