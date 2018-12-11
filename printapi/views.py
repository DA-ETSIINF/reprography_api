import datetime
import math
from django.core.mail import EmailMessage


from django.shortcuts import render
import os
from PyPDF2 import PdfFileReader
# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from printapi.models import File, Folder, History
from printapi.serializers import FilesSerializer, UserFilesSerializer, HomeSerializer, HistorySerializer


class CreateFileView(CreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = FilesSerializer
    queryset = File.objects.all()

    def post(self, request, *args, **kwargs):
        filename, filetype = os.path.splitext(str(self.request.data['file']))

        serializer = FilesSerializer(data=self.request.data)
        if serializer. is_valid():
            if filetype != '.pdf':
                return Response({'response': 'It´s not a valid file'}, status=status.HTTP_400_BAD_REQUEST)
            file = File.objects.create(
                file=self.request.data['file'],
                name=str(self.request.data['file']),
                folder=Folder.objects.filter(owner=self.request.user, root=True)[0]
            )
            file.create()
            return Response({'response': 'File uploaded'}, status=status.HTTP_200_OK )
        return Response({'response': 'Incorrect data'}, status=status.HTTP_406_NOT_ACCEPTABLE)



class HomeView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HomeSerializer

    def get_queryset(self):
        return Folder.objects.all().filter(owner=self.request.user, root=True)


class UpdateFileView(DestroyAPIView):
    pass


def mail(pdfname, pdf):
    email = EmailMessage('', '', 'tryit.da@fi.upm.es', ['oyd43ouka256@hpeprint.com'])

    email.attach(pdfname, pdf, 'application/pdf')
    email.send()

class PrintDocument(CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HistorySerializer
    queryset = History.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = HistorySerializer(data=self.request.data)
        if serializer.is_valid():
            user = self.request.user
            document_id = self.request.data['documentId']
            try:
                double_sided = True if self.request.data['doubleSided'] == 'true' else False
            except:
                double_sided = False
            file = File.objects.get(id=document_id)
            npages = file.npages
            date = datetime.datetime.now()
            # We use the npages of a document to retrieve the amount to pay.
            topay =  math.ceil(npages / 2) * 0.4 if double_sided else npages * 0.4
            # they only have to pay for sheet, so if they print double sided, a sheet is 2 sided.

            History.objects.create(
                user=user,
                documentId=file,
                npages=npages,
                amount=topay,
                doubleSided=double_sided,
                date=date,
            )
            #file.create()
            mail(file.name, file.file.read())

            return Response({'response': 'Printing document'}, status=status.HTTP_200_OK)
        return Response({'response': 'Incorrect data'}, status=status.HTTP_406_NOT_ACCEPTABLE)

## Createfolder