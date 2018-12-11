import datetime

from PyPDF2 import PdfFileReader
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Funds(models.Model):
    amount = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, )


class Folder(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, )
    folder = models.ForeignKey(to='Folder', related_name='+', on_delete=models.CASCADE, default=1, blank=True, null=True)
    root = models.BooleanField(default=False, blank=False, null=False)


    def __str__(self):
        return self.name + " || " + str(self.folder) + " || " + str(self.owner) + " || " + str(self.root)


class File(models.Model):
    folder = models.ForeignKey(Folder, models.CASCADE)
    file = models.FileField(default="")
    name = models.CharField(max_length=50, default="PracticaEstructura", null=True, blank=True)
    npages = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(self.file) + " || " + str(self.folder)

    '''
    When a new file is uploaded we get it's number of pages before creating the model.
    '''
    def create(self, *args, **kwargs):
        if self.file:
            pdf = PdfFileReader(open(str(self.file.path), 'rb'))
            self.npages = pdf.getNumPages()
        super(File, self).save(*args, **kwargs)



class FundTransaction(models.Model):
    found = models.ForeignKey(User, on_delete=models.CASCADE, )
    #tipos
    type = models.CharField(max_length=30) # must be select options
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    amount = models.FloatField()
    file = models.ForeignKey(Folder, blank=True, null=True, on_delete=models.PROTECT, default=0)


class History(models.Model):
    date = models.DateTimeField()
    documentId = models.ForeignKey(File, on_delete=models.PROTECT, default=0)
    npages = models.IntegerField()
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    doubleSided = models.BooleanField(default=False)



