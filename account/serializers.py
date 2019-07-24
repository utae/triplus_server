from django.contrib.auth import get_user_model
from rest_framework import serializers


# Get the User model
UserModel = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'profile_img',)
