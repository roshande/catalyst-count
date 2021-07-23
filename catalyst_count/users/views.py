from rest_framework import viewsets
from django.views import View
from django.views.generic.base import TemplateResponseMixin, TemplateView
from django.contrib.auth.models import User
from rest_framework import generics
from django.shortcuts import render
#from datatableview.views import DatatableView

from .serializer import UserSerializer

# Create your views here.


#class UserDatatableView(DatatableView):
#    model = User

class UserViewset(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTemplateView(TemplateView):
    template_name = "users/user_list.html"
