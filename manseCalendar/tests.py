# Create your tests here.
import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Day

class MansecalendarTestcase(APITestCase):

    TEST_DAY = {
        "year": 1984,
        "month": 6,
        "day": 8,
        "date": datetime.date(1984, 6, 8),
        "week_day": 4,
        "lunar_year": 1984,
        "lunar_month": 5,
        "lunar_day": 9,
        "is_lunar_leap_month": False,
        "is_solar_term": False,
        "year_heaven_letter": "甲",
        "year_ground_letter": "子",
        "month_heaven_letter": "庚",
        "month_ground_letter": "午",
        "day_heaven_letter": "癸",
        "day_ground_letter": "酉"
    }

    def setUp(self):
        self.a_day = Day.objects.create(**MansecalendarTestcase.TEST_DAY)
        self.url_get_day = reverse('get_day', kwargs={'year': str(MansecalendarTestcase.TEST_DAY['year']),
                                                      'month': str(MansecalendarTestcase.TEST_DAY['month']),
                                                      'day': str(MansecalendarTestcase.TEST_DAY['day'])})

    def test_get_day(self):
        response = self.client.get(self.url_get_day, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


