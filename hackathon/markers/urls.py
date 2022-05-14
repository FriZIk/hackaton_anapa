from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MarkerImageBase64, MarkerList, MarkerDetail, MarkerUpload, MarkerUploadArchive

urlpatterns = [
  path('markers/', MarkerList.as_view(), name='markers'),
  path('markers/upload/', MarkerUpload.as_view(), name='markers_upload'),
  path('markers/upload/as_archive/', MarkerUploadArchive.as_view(), name='markers_archive_upload'),
  path('markers/<int:pk>/', MarkerDetail.as_view(), name='marker_detail'),
  path('markers/<int:pk>/get_image_base64/', MarkerImageBase64.as_view(), name='marker_image_base64'),
]