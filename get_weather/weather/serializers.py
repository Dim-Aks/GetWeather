from rest_framework import serializers

from .models import CitySearch


class CitySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitySearch
        fields = '__all__'