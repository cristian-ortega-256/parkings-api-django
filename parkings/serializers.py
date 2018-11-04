from rest_framework import serializers
from .models import Parkings


class ParkingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkings
        fields = ("id","x", "y","isOccupied")