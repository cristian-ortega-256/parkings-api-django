from rest_framework import serializers
from .models.Parkings import Parkings
from .models.Configuration import Configuration

class ParkingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkings
        fields = ("id","x", "y","isOccupied")

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ("key","value")