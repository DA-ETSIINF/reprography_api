from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from printapi.models import File, Folder, History


class FilesSerializer(ModelSerializer):
    class Meta:
        model= File
        fields= ('id', 'name', 'npages', 'file', )




class HomeSerializer(ModelSerializer):

    files = serializers.SerializerMethodField()

    def get_files(self, folder):
        print(folder.id)
        query = File.objects.all().filter(folder=folder.id)
        return FilesSerializer(query.prefetch_related().all(),
                               many=True, context=self.context).data

    folders = serializers.SerializerMethodField()

    def get_folders(self, folder):
        print("folder" + str(folder.id))
        query = Folder.objects.all().filter(owner=self.context['request'].user,  folder=folder.id)
        return FolderSerializer(query.prefetch_related().all(),  many=True, context=self.context).data

    class Meta:
        model = Folder
        fields = ('name',  'id', 'folders', 'files',)



class HistorySerializer(ModelSerializer):

    class Meta:
        model = History
        fields = ('documentId', 'doubleSided', 'color')



class UserFilesSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('folder', 'file', 'id')


class FolderSerializer(ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'

