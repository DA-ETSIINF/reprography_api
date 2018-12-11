from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class UserProfile(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FilesSerializer

    def get_queryset(self):
        return  User.objects.all().filter(id=self.request.user.id)