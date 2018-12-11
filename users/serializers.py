from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from printapi.models import File, Folder, History, Funds


class UserSerializer(ModelSerializer):

    funds = serializers.SerializerMethodField()

    def get_funds(self, folder):
        print(folder.id)
        query = Funds.objects.all().filter(owner=self.context['request'].user)
        return query.values('amount')[0]['amount'] if len(query) != 0 else 0.0

    class Meta:
        model= User
        fields= ('id', 'username', 'email', 'funds', )



