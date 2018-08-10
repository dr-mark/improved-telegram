from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .serializers import FileUploadSerializer

from .models import FileUpload


class ViewPermissionsMixin(object):
    """
    Base class for all custom permission mixins to inherit from
    """
    def has_permissions(self):
        # Can use self.get_object() and self.request.user here
        return True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise PermissionDenied
        return super(ViewPermissionsMixin, self).dispatch(
            request, *args, **kwargs)


class FileUploadDetail(LoginRequiredMixin, ViewPermissionsMixin, DetailView):
    model = FileUpload

    def has_permissions(self):
        return self.request.user == self.get_object().created_by or self.get_object().public


class FileUploadList(LoginRequiredMixin, ListView):
    context_object_name = 'file_upload_list'

    def get_queryset(self):
        """
        Limit the FileUpload objects listed to those that the
        current user has permission to view.
        :return: queryset
        """
        return FileUpload.objects.for_user(self.request.user)


class FileUploadCreate(LoginRequiredMixin, CreateView):
    model = FileUpload
    fields = ['description', 'file', 'public']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(FileUploadCreate, self).form_valid(form)


class FileUploadViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows file uploads to be viewed
    """
    queryset = FileUpload.objects.all().order_by('-created_at')
    serializer_class = FileUploadSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('file',)

    def get_queryset(self):
        """
        Limit the FileUpload objects listed to those that the
        current user has permission to view.
        :return: queryset
        """
        return FileUpload.objects.for_user(self.request.user).order_by('-created_at')
