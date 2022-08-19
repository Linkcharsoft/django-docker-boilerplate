from rest_framework import serializers
from users.models import User_profile, User

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
        read_only_fields = ('email', 'date_joined', 'id', 'username')

class User_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = '__all__'
        read_only_fields = ('user',)
