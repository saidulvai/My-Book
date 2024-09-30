from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user_type']
        
class UserSerializer(serializers.ModelSerializer):
    account = serializers.StringRelatedField()
    account = AccountSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'account']


class RegstrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        user_type = self.validated_data['user_type']
        password = self.validated_data['password'] 
        password2 = self.validated_data['confirm_password'] 

        if password != password2:
            raise serializers.ValidationError({'error': 'password does not match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        user = User(username=username, email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.is_active = False
        user.save()

        account = Account(user=user, user_type=user_type)
        account.save()
        return user
    
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source="account", many=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile')

        # Custom .update() method for serializer to handle UserProfile data update
        def update(self, instance, validated_data):
            userprofile_serializer = self.fields['profile']
            userprofile_instance = instance.userprofile
            userprofile_data = validated_data.pop('userprofile', {})

            # to access the UserProfile fields in here
            # mobile = userprofile_data.get('mobile')

            # update the userprofile fields
            userprofile_serializer.update(userprofile_instance, userprofile_data)

            instance = super().update(instance, validated_data)
            return instance