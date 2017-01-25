from rest_framework.serializers import ModelSerializer

from .models import Day


class DaySerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ["year",
                  "month",
                  "day",
                  "date",
                  "week_day",
                  "lunar_year",
                  "lunar_month",
                  "lunar_day",
                  "is_lunar_leap_month",
                  "is_solar_term",
                  "year_heaven_letter",
                  "year_ground_letter",
                  "month_heaven_letter",
                  "month_ground_letter",
                  "day_heaven_letter",
                  "day_ground_letter"]
        read_only_fields = fields
