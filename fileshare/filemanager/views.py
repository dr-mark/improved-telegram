from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import FileUpload


class FileUploadDetail(DetailView):
    model = FileUpload


class FileUploadList(ListView):
    model = FileUpload
    context_object_name = 'file_upload_list'
