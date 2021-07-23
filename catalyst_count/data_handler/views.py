from rest_framework import viewsets
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse

from .uploadhandler import ProgressBarUploadHandler
from .forms import UploadFileForm, QueryBuilderForm
from .file_data_handler import handle_uploaded_file
from .models import Companies
from .serializer import CompanySerializer

# Create your views here.


@method_decorator(csrf_exempt, 'dispatch')
class UploadFile(FormView):
    form_class = UploadFileForm
    template_name = "account/upload.html"
    success_url = "/data/upload_data/"

    def post(self, request):
        request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
        return self._upload_file_view(request)

    @method_decorator(csrf_protect)
    def _upload_file_view(self, request):
        form = self.get_form()
        print(form.is_valid())
        if not form.is_valid():
            print("invalid form")
            return self.form_invalid(form)
        uploaded_file = request.FILES.get('file', None)
        print("uploaded file", uploaded_file)
        if uploaded_file is None:
            return reverse("upload_file")
        handle_uploaded_file(uploaded_file)
        print("handling of data file completed")
        return self.form_valid(form)


class QueryBuilder(FormView):
    form_class = QueryBuilderForm
    template_name = "account/query_builder.html"

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer

