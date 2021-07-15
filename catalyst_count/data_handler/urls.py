from django.urls import path, include
from .views import UploadFile, QueryBuilder

urlpatterns = [
    path('upload_data/', UploadFile.as_view(), name="upload_file"),
    path('query_builder/', QueryBuilder.as_view(), name="query_builder"),
]
