from django.db import models
from accounts.models import Faculty

class Course(models.Model):

    course_name = models.CharField(max_length=100)

    description = models.TextField()

    duration = models.CharField(max_length=50)

    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name="courses")

    def __str__(self):

        return self.course_name