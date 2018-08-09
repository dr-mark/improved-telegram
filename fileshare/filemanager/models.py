from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


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

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('filemanager:detail', kwargs={'pk': self.pk})
