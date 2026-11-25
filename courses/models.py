from django.db import models
from accounts.models import Faculty

class Course(models.Model):

    course_name = models.CharField(max_length=100)

    description = models.TextField()

    duration = models.CharField(max_length=50)

    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name="courses")

class Module(models.Model):

    title = models.CharField(max_length = 100)

    description = models.TextField(null = True)

    course = models.ForeignKey(Course,on_delete = models.CASCADE,related_name = "modules")
    