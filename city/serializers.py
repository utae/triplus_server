from rest_framework import serializers

from hash_tag.serializers import HashTagSerializer
from .models import City


class CitySerializer(serializers.ModelSerializer):

    hash_tag_set = HashTagSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'
