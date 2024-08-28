from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ["id", "username", "password"]
    #     extra_kwargs= {"password": {"write_only":True}}
    password1 = serializers.CharField(write_only=True,  validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'password1', 'password2']
        extra_kwargs= {"password1": {"write_only":True}, "password2": {"write_only":True}}

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            
            username=validated_data['username'],
                        
        )

        
        user.set_password(validated_data['password1'])
        user.save()
        return user

