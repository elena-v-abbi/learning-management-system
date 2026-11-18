from django.shortcuts import render
from .models import User
from rest_framework import authentication,permissions
from .serializer import UserSerializer,FacultySerializer
from .permissions import IsFaculty

from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
# Create your views here.

class UserCreateView(CreateAPIView):

    serializer_class=UserSerializer

class FacultyProfileView(RetrieveUpdateAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[IsFaculty]

    serializer_class=FacultySerializer

    def get_object(self):

        obj = self.request.user.faculty_member

        self.check_object_permissions(self.request,obj)

        return obj