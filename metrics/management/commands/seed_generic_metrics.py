import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from metrics.models import GenericMetric


class Command(BaseCommand):
    help = "Seed synthetic generic CI/CD metrics for GitHub Actions, Jenkins, and AWS CodePipeline"

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=5,
            help="How many days of history to generate (default: 5)",
        )
        parser.add_argument(
            "--per-day",
            type=int,
            default=5,
            help="How many pipeline runs per tool per day (default: 5)",
        )

    def handle(self, *args, **options):
        days = options["days"]
        per_day = options["per_day"]

        tools = ["GitHub Actions", "Jenkins", "AWS CodePipeline"]

        # Optional: clear existing data for a clean demo
        GenericMetric.objects.all().delete()

        now = timezone.now()
        created_count = 0

        for day_offset in range(days):
            day_base = now - timedelta(days=day_offset)

            for tool in tools:
                for i in range(per_day):
                    # Fake timestamps for that day
                    ts = day_base.replace(
                        hour=random.randint(8, 22),
                        minute=random.randint(0, 59),
                        second=random.randint(0, 59),
                        microsecond=0,
                    )

                    # Synthetic values with slight differences per tool
                    if tool == "GitHub Actions":
                        build_time = random.uniform(30, 90)
                        tests_total = random.randint(50, 120)
                        failed_tests = random.randint(0, 5)
                        coverage = random.uniform(75, 95)
                        success = random.choices([True, False], weights=[85, 15])[0]
                    elif tool == "Jenkins":
                        build_time = random.uniform(40, 110)
                        tests_total = random.randint(60, 140)
                        failed_tests = random.randint(0, 8)
                        coverage = random.uniform(70, 92)
                        success = random.choices([True, False], weights=[80, 20])[0]
                    else:  # AWS CodePipeline
                        build_time = random.uniform(35, 100)
                        tests_total = random.randint(40, 100)
                        failed_tests = random.randint(0, 6)
                        coverage = random.uniform(72, 94)
                        success = random.choices([True, False], weights=[82, 18])[0]

                    GenericMetric.objects.create(
                        tool=tool,
                        build_time_sec=round(build_time, 2),
                        tests_total=tests_total,
                        failed_tests=failed_tests,
                        coverage_percent=round(coverage, 2),
                        success_rate=100.0 if success else random.uniform(70.0, 95.0),
                        timestamp=ts,
                    )

                    created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {created_count} GenericMetric rows "
                f"for tools: {', '.join(tools)} over {days} days."
            )
        )
