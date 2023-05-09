from rest_framework import serializers
from .models import * 


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnTable
        fields = '__all__'