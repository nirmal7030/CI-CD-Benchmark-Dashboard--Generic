from django.urls import path
from . import views

urlpatterns = [
    # HTML dashboard at /
    path("", views.generic_dashboard, name="generic-dashboard"),

    # API endpoints
    path("api/generic/ingest/", views.generic_ingest, name="generic-ingest"),
    path("api/generic/metrics/", views.generic_metrics_data, name="generic-metrics-data"),
]
