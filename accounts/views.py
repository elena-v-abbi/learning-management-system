from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.

class UserCreateView(CreateAPIView):

    serializer_class=UserSerializer