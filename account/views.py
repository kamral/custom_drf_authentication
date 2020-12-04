from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
# Create your views here.
from .serializers import UserRegistrationSerializers, \
    UserLoginSerializers,UserApiAuthSerializers
from .models import User

class UserRegistrApiView(ListCreateAPIView):
    serializer_class =UserRegistrationSerializers
    queryset = User.objects.all()

class UserLoginApiVIew(ListCreateAPIView):
    serializer_class = UserLoginSerializers
    queryset = User.objects.all()


class UseApiAuthView(ListCreateAPIView):
    serializer_class = UserLoginSerializers
    queryset = User.objects.all()

