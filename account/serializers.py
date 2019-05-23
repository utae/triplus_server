from django.contrib.auth import get_user_model
from rest_framework import serializers


# Get the User model
UserModel = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'username',)
        read_only_fields = ('email', )
