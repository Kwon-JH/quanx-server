# -*- coding: utf-8 -*-

import codecs
import datetime

from django.core.management import BaseCommand

from manseCalendar.models import Day, ManseConstants


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        Command.update_letters(*args, **options)

    @classmethod
    def update_letters(cls, *args, **kwargs):
        Command.get_day_letter()
        Command.get_month_letter()

    @classmethod
    def get_day_letter(cls):
        day_zero = datetime.date(1984, 6, 8)
        zero_heaven_letter = u'癸'
        zero_ground_letter = u'酉'

        for day in Day.objects.filter(date__gte=datetime.date(1984, 6, 1))[:20]:
            diff_in_days = (day.date - day_zero).days
            zero_heaven_letter_index = ManseConstants.HEAVEN_LETTERS_INDEX[zero_heaven_letter] - 1
            zero_ground_letter_index = ManseConstants.GROUND_LETTERS_INDEX[zero_ground_letter] - 1

            mod10 = abs(diff_in_days) % 10
            mod12 = abs(diff_in_days) % 12

            mod10 = [mod10, -mod10][diff_in_days < 0]
            mod12 = [mod10, -mod12][diff_in_days < 0]

            heaven_index = (zero_heaven_letter_index + mod10) % 10
            ground_index = (zero_ground_letter_index + mod12) % 12

            day_heaven_letter = ManseConstants.HEAVEN_LETTERS[heaven_index]
            day_ground_letter = ManseConstants.GROUND_LETTERS[ground_index]

            print diff_in_days, day_heaven_letter, day_ground_letter

    @classmethod
    def get_month_letter(cls):
        month

        pass

    @classmethod
    def get_year_letter(cls, day):
        pass
