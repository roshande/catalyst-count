from .models import Companies
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        lookup_field = 'uuid'
        readonly = 'uuid'
        fields = '__all__'
