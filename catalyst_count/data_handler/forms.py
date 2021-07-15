from django import forms
from .models import Companies

class UploadFileForm(forms.Form):
    file = forms.FileField(
        required=True, localize=True,
        widget=forms.FileInput(attrs={"class": "form-control-file"}))

class IndustrySelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(args, kwargs)
        if value:
            option['attrs']['data'] = 1
        return option

class QueryBuilderForm1(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['name', 'industry','year_founded', 'locality', 'country' ]
        #widgets = {'keyword': }

class QueryBuilderForm(forms.Form):
    keyword = forms.CharField()
    #industry = forms.ModelChoiceField(queryset=Companies.objects.order_by().values('industry').distinct())
    year_founded = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    employees_from = forms.IntegerField()
    employees_to = forms.IntegerField()
