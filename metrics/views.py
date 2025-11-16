from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import GenericMetric
from .serializers import GenericMetricSerializer


def generic_dashboard(request):
    return render(request, "metrics/dashboard.html")


@api_view(["POST"])
def generic_ingest(request):
    """
    Expected JSON body (example):

    {
      "tool": "github",          # or "jenkins" or "codepipeline"
      "build_time_sec": 5.3,
      "test_time_sec": 2.1,
      "total_time_sec": 7.6,
      "failed_tests": 0,
      "success_rate": 1.0
    }
    """
    serializer = GenericMetricSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "ok"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def generic_metrics_data(request):
    """
    Optional query param: ?tool=github|jenkins|codepipeline
    """
    tool = request.GET.get("tool")
    qs = GenericMetric.objects.all()
    if tool:
        qs = qs.filter(tool=tool)

    qs = qs[:50]  # latest 50
    serializer = GenericMetricSerializer(qs, many=True)
    return Response(serializer.data)
