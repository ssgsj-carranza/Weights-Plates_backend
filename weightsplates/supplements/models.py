from django.db import models

# Create your models here.


class Supplements(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    side_effects = models.CharField(max_length=300)
