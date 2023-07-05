from rest_framework import serializers
from .models import * 


class TotalQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryModel
        fields = '__all__'