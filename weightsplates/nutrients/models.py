from django.db import models


class Nutrients(models.Model):
    name = models.CharField(max_length=50)
    serving_size = models.CharField(max_length=500)
    protein = models.CharField(max_length=500)
    carbs = models.CharField(max_length=500)
    fats = models.CharField(max_length=500)
    calories = models.CharField(max_length=500)