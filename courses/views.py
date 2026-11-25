from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsFaculty
from .models import Course
from .serializer import CourseSerializer,ModuleSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.permissions import IsCourseFaculty



class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsCourseFaculty]

    serializer_class = CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(faculty__user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(faculty=self.request.user.faculty_member)


class CourseDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsCourseFaculty]

    serializer_class=CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(faculty__user=self.request.user)


class ModuleCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [IsCourseFaculty]
    
    def post(self,request,pk = None):
    
        form_data = request.data
    
        course_object = get_object_or_404(Course,id = pk)

        serializer_instance=ModuleSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(course=course_object)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
