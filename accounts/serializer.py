from rest_framework import serializers
from .models import User,Student,Faculty

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","password","email","phone","role"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

class FacultySerializer(serializers.ModelSerializer):

    class Meta:

        model=Faculty

        fields="__all__"