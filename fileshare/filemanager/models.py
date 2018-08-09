from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import get_user_model


class FileUploadManager(models.Manager):
    def for_user(self, user):
        """
        Return FileUploads where either the FileUpload was created by
        the given user, or the FileUpload is marked as public.
        :param user: a Django user
        :return: queryset
        """
        return super(FileUploadManager, self).get_queryset().filter(
            Q(created_by=user) | Q(public=True))


class FileUpload(models.Model):
    """
    This model represents a file upload
    """
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/')
    public = models.BooleanField()
    created_by = models.ForeignKey(get_user_model())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FileUploadManager()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('filemanager:detail', kwargs={'pk': self.pk})
