from django.db import models


class Supplements(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    side_effects = models.CharField(max_length=500)
