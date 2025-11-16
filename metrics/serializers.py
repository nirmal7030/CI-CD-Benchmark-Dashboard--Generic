from rest_framework import serializers
from .models import GenericMetric


class GenericMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericMetric
        fields = "__all__"
