from rest_framework import serializers
from .models import * 


class AppDownloadLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDownloadLogModel
        fields = '__all__'