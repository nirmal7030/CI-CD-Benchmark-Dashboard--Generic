from django.db import models


class GenericMetric(models.Model):
    TOOL_CHOICES = [
        ("github", "GitHub Actions"),
        ("jenkins", "Jenkins"),
        ("codepipeline", "AWS CodePipeline"),
    ]

    tool = models.CharField(
        max_length=32,
        choices=TOOL_CHOICES,
        default="github",   # ✅ this avoids the migration prompt
    )

    build_time_sec = models.FloatField(default=0.0)
    test_time_sec = models.FloatField(default=0.0)
    total_time_sec = models.FloatField(default=0.0)

    failed_tests = models.IntegerField(default=0)
    success_rate = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_tool_display()} run @ {self.created_at} – {self.total_time_sec:.2f}s"
