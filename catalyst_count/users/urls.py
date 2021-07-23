from rest_framework import routers
from django.urls import path, include

from .views import UserViewset, UserTemplateView

router = routers.DefaultRouter()
router.register('user', UserViewset)

urlpatterns = [
    path('', UserTemplateView.as_view(), name='user_list'),
    path('user', include(router.urls)),
]
