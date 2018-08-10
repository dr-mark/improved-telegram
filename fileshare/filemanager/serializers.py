from rest_framework import serializers

from .models import FileUpload


class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('description', 'file', 'public', 'created_at')

