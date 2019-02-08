from django.contrib import admin
from django.urls import path, include

from printapi.views import HomeView, CreateFileView, PrintDocument
from users.views import UserProfile

urlpatterns = [
    #path('', HomeView.as_view(), name="print-index"),
    path('profile/', UserProfile.as_view(),  name="print-documents"),
]
