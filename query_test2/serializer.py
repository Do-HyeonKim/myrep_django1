from rest_framework import serializers
from .models import * 


class TotalQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalQuery
        fields = '__all__'