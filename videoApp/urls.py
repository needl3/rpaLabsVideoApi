from django.urls import include, path
from . import views
from . import viewsApi

app_name = 'videoApp'
urlpatterns = [
    # Api endpoints
    # Views are defined in ./viewsApi.py file
    path('api/upload/', viewsApi.upload, name='apiUpload'),
    path('api/listUploading/', viewsApi.listUploading, name='apiListUploading'),
    path('api/charge/', viewsApi.charge, name='apiCharge'),
    path('api', viewsApi.listUploaded, name='apiListUploaded'),
    path('', views.index, name='apiIndex'),
]
