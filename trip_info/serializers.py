from rest_framework import serializers

from account.serializers import AuthorSerializer
from hash_tag.serializers import HashTagSerializer
from trip_info.models import TripInfo


class TripInfoSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    hash_tag_set = HashTagSerializer(many=True, read_only=True)

    class Meta:
        model = TripInfo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_modified_at',)
