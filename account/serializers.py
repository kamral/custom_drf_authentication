from rest_framework import serializers
from .models import User

class UserRegistrationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('username','first_name','last_name','age', 'password')

    def create(self, validated_data):
        user = super(UserRegistrationSerializers, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('username','first_name','last_name','password')

class UserApiAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name', 'password')
