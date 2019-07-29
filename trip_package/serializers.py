from rest_framework import serializers

from account.serializers import AuthorSerializer
from hash_tag.serializers import HashTagSerializer
from guide.serializers import GuideSerializer

from .models import TripPackage


class TripPackageSerializer(serializers.ModelSerializer):

    guide = GuideSerializer(read_only=True)
    hash_tag_set = HashTagSerializer(many=True, read_only=True)

    class Meta:
        model = TripPackage
        fields = '__all__'
        read_only_fields = ('created_at', 'last_modified_at',)
