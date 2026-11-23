from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializer import CourseSerializer


class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(faculty__user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(faculty=self.request.user.faculty_member)


class CourseDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(faculty__user=self.request.user)