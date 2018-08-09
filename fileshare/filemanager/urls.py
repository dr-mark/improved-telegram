from django.conf.urls import include, url

from .views import FileUploadDetail, FileUploadList


app_name = 'filemanager'
urlpatterns = [
    url(r'^$', FileUploadList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', FileUploadDetail.as_view(), name='detail'),
]
