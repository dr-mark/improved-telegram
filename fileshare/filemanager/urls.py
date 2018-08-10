from django.conf.urls import include, url

from rest_framework import routers

from .views import FileUploadDetail, FileUploadList, FileUploadCreate, FileUploadViewSet

router = routers.DefaultRouter()
router.register(r'fileuploads', FileUploadViewSet)

app_name = 'filemanager'
urlpatterns = [
    url(r'^$', FileUploadList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', FileUploadDetail.as_view(), name='detail'),
    url(r'^add/$', FileUploadCreate.as_view(), name='create'),
]
