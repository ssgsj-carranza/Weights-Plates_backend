from rest_framework import serializers
from .models import Supplements


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplements
        fields = ['id', 'name', 'description', 'side_effects']
