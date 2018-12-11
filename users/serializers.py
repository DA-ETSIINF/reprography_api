from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from printapi.models import File, Folder, History


class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields= ('id', 'username', 'npages', 'file', )



