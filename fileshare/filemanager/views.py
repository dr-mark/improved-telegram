from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from .models import FileUpload


class FileUploadDetail(DetailView):
    model = FileUpload


class FileUploadList(ListView):
    model = FileUpload
    context_object_name = 'file_upload_list'


class FileUploadCreate(CreateView):
    model = FileUpload
    fields = ['description', 'file', 'public']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(FileUploadCreate, self).form_valid(form)