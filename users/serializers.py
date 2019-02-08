from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from printapi.models import File, Folder, History, Funds


class UserSerializer(ModelSerializer):

    funds = serializers.SerializerMethodField()

    def get_funds(self, user):
        return Funds.objects.all().filter(owner=user)[0].amount

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'funds')



