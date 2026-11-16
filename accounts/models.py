from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=12,unique=True)

    ROLE_CHOICES=(
        ("Faculty","Faculty"),
        ("Student","Student")
    )

    role=models.CharField(max_length=200,choices=ROLE_CHOICES)

class Studenet(models.Model):

    age=models.CharField(max_length=2)

    GENDER_CHOICES=(
        ("male","male"),
        ("female","female")
    )

    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)

    dob=models.DateField(null=True)

    department=models.CharField(max_length=50,null=True)

    college=models.CharField(max_length=100,null=True)

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Students")

class Faculty(models.Model):

    qualification=models.CharField(max_length=100)

    experience=models.CharField(max_length=50)

    GENDER_CHOICES=(
            ("male","male"),
            ("female","female")
        )

    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="faculty_member")

