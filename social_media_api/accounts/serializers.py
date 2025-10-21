# accounts/serializers.py
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    # This ensures 'password' is write-only and is handled by create_user
    password = serializers.CharField(write_only=True) 
    serializers.CharField()
    get_user_model().objects.create_user
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # 2. Directly using the imported User model's manager method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', '')
        )
        # 3. No manual Token.objects.create needed here!
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    # This serializer is used for displaying user details and relationships (Task 2)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'following', 'followers')
        read_only_fields = ('id', 'username', 'email', 'followers')
