from django.urls import path, include
from rest_framework import routers

from .views import UploadFile, QueryBuilder, CompanyViewSet

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload_data/', UploadFile.as_view(), name="upload_file"),
    path('query_builder/', QueryBuilder.as_view(), name="query_builder"),
]
