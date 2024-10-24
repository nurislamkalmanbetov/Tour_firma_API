from rest_framework import serializers
from .models import User, Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'avatar', 'is_active', 'is_staff')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            avatar=validated_data.get('avatar', None),
            is_active=validated_data.get('is_active', True),
            is_staff=validated_data.get('is_staff', True)
        )
        return user
    

class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom fields to the token
        token['username'] = user.username
        return token
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user', 'first_name', 'last_name',
            'birth_date', 'profile_image', 'status',
            'phone', 'country'
        )