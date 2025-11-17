from django.db import models


class GenericMetric(models.Model):
    TOOL_CHOICES = [
        ("GitHub Actions", "GitHub Actions"),
        ("Jenkins", "Jenkins"),
        ("AWS CodePipeline", "AWS CodePipeline"),
    ]

    # Which CI/CD tool produced this metric
    tool = models.CharField(max_length=50, choices=TOOL_CHOICES)

    # Generic metrics we want to compare
    build_time_sec = models.FloatField(default=0.0)       # pipeline / build time
    tests_total = models.IntegerField(default=0)          # total tests run
    failed_tests = models.IntegerField(default=0)         # failed tests
    coverage_percent = models.FloatField(default=0.0)     # test coverage %
    success_rate = models.FloatField(default=0.0)         # success rate %

    # When this run happened
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.tool} @ {self.timestamp} – {self.build_time_sec}s"
