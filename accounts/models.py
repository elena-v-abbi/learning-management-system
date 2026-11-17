from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=12,unique=True)

    ROLE_CHOICES=(
        ("Faculty","Faculty"),
        ("Student","Student")
    )

    role=models.CharField(max_length=200,choices=ROLE_CHOICES)

class Student(models.Model):

    age=models.CharField(max_length=2,blank=True)

    GENDER_CHOICES=(
        ("male","male"),
        ("female","female")
    )

    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,blank=True)

    dob=models.DateField(null=True,blank=True)

    department=models.CharField(max_length=50,null=True,blank=True)

    college=models.CharField(max_length=100,null=True,blank=True)

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Students")

class Faculty(models.Model):

    qualification=models.CharField(max_length=100,blank=True)

    experience=models.CharField(max_length=50,blank=True)

    GENDER_CHOICES=(
            ("male","male"),
            ("female","female")
        )

    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,blank=True)

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="faculty_member")

def create_profile(sender,instance,created,**kwargs):

    if created:

        if instance.role=="Faculty":

            Faculty.objects.create(user=instance)

        elif instance.role=="Student":

            Student.objects.create(user=instance)

post_save.connect(create_profile,sender=User)
