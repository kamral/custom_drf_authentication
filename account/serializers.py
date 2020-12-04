from rest_framework import serializers
from .models import User

class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name','last_name','age', 'password')

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name','last_name','age')

class UserApiAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name', 'password')
