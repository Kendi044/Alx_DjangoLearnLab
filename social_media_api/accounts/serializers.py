# accounts/serializers.py
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    # This ensures password is write-only and not returned in the response
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # 🔑 Using User.objects.create_user directly
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', '')
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    # This serializer is used for displaying user details (Task 2)
    # Note: 'followers' is automatically available due to related_name on the 'following' field
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'following', 'followers')
        read_only_fields = ('id', 'username', 'email', 'followers')
