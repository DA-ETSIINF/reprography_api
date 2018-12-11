from django.contrib import admin
from django.urls import path, include

from printapi.views import HomeView, CreateFileView, PrintDocument

urlpatterns = [
    path('', HomeView.as_view(), name="print-index"),
    path('files/', HomeView.as_view(),  name="print-documents"),
    path('upload/', CreateFileView.as_view(), name="print-documents"),
    path('send-to-printer/', PrintDocument.as_view(),  name="send-to-printer")

]
