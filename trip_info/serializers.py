from rest_framework import serializers

from account.serializers import AuthorSerializer
from hash_tag.serializers import HashTagSerializer
from city.serializers import CitySerializer
from .models import TripInfo, TripInfoDetail


class TripInfoSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    hash_tag_set = HashTagSerializer(many=True, read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = TripInfo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_modified_at',)


class TripInfoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TripInfoDetail
        fields = '__all__'

