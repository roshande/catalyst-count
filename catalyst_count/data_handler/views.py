from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .uploadhandler import ProgressBarUploadHandler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django_q.tasks import AsyncTask, async_task
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render
from .forms import UploadFileForm, QueryBuilderForm
from .file_data_handler import handle_uploaded_file

# Create your views here.
class UploadFile(View):

    @method_decorator(csrf_exempt)
    def post(self, request):
        #request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
        if request.is_ajax():
            return self._upload_file_view(request)
        return HttpResponseRedirect()

    @method_decorator(csrf_protect)
    def _upload_file_view(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #task_id = async_task('handle_uploaded_file', request.FILES['file'],
            #                     hook='',
            #                     group='file_upload')
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('upload-data'))
        return HttpResponseRedirect(reverse('upload-data'))

    def get(self, request):
        context = {
            'form' : UploadFileForm()
        }
        return render(request, 'account/upload.html', context)


class QueryBuilder(View):
    def get(self, request):
        context = {
            'form' : QueryBuilderForm()
        }
        return render(request, 'account/query_builder.html', context)

    def post(self, request, format=None):
        pass
