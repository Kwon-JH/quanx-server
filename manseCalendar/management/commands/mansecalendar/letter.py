# -*- coding: utf-8 -*-

import datetime

from django.core.management import BaseCommand
from django.db import transaction

from manseCalendar.models import Day, ManseConstants, SolarTerm


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)


    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        Command.update_letters(*args, **options)

    @classmethod
    def update_letters(cls, *args, **kwargs):
        # Command.get_day_letter()
        # Command.get_year_letter()
        # Command.get_solarterm_letter()
        Command.get_month_letter()

    @classmethod
    def get_day_letter(cls):
        day_zero = datetime.date(1984, 6, 8)
        zero_heaven_letter = u'癸'
        zero_ground_letter = u'酉'

        with transaction.atomic():
            for day in Day.objects.all():
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

                # print diff_in_days, day_heaven_letter, day_ground_letter
                day.day_heaven_letter = day_heaven_letter
                day.day_ground_letter = day_ground_letter
                day.save()

    @classmethod
    def get_solarterm(cls, year, julki_name):
        solarterm = SolarTerm.objects.get(time__gte=datetime.datetime(year, 1, 1),
                                          time__lte=datetime.datetime(year, 12, 31),
                                          name=julki_name)
        return solarterm

    @classmethod
    def get_solarterm_letter(cls):

        with transaction.atomic():
            for year in range(1800, 2051):
                spring_jul_heaven_letter = Command.get_spring_jul_heaven_letter(year)
                spring_jul_heaven_index = ManseConstants.HEAVEN_LETTERS_INDEX[spring_jul_heaven_letter] - 1
                spring_jul_ground_index = 2

                for solarterm in SolarTerm.objects.filter(time__gte=datetime.datetime(year, 1, 1),
                                                          time__lt=datetime.datetime(year + 1, 1, 1)):
                    julki_index = ManseConstants.JULKI_INDEX[solarterm.name]

                    if julki_index % 2 != 0:
                        julki_index -= 1

                    jul_index = julki_index / 2

                    spring_jul_index = 1
                    index_diff = jul_index - spring_jul_index

                    solarterm_heaven_letter_index = (spring_jul_heaven_index + index_diff)

                    if solarterm_heaven_letter_index >= 10:
                        solarterm_heaven_letter_index %= 10

                    solarterm_ground_letter_index = (spring_jul_ground_index + index_diff)

                    if solarterm_ground_letter_index >= 12:
                        solarterm_ground_letter_index %= 12

                    solarterm.month_heaven_letter = ManseConstants.HEAVEN_LETTERS[solarterm_heaven_letter_index]
                    solarterm.month_ground_letter = ManseConstants.GROUND_LETTERS[solarterm_ground_letter_index]
                    solarterm.save()


    @classmethod
    def get_month_letter(cls):

        with transaction.atomic():
            prev_solarterm = None

            for solarterm in SolarTerm.objects.all():
                if not prev_solarterm:
                    prev_solarterm = solarterm
                    continue

                prev_solarterm_date = prev_solarterm.time.date()
                solarterm_date = solarterm.time.date()
                for day in Day.objects.filter(date__gte=prev_solarterm_date,
                                              date__lt=solarterm_date):
                    day.month_heaven_letter = prev_solarterm.month_heaven_letter
                    day.month_ground_letter = prev_solarterm.month_ground_letter

                    if day.date == prev_solarterm_date:
                        day.is_solar_term = True

                    day.save()

                prev_solarterm = solarterm


    @classmethod
    def get_year_letter(cls):
        day_zero = datetime.date(1984, 6, 8)
        zero_heaven_letter = u'甲'
        zero_ground_letter = u'子'

        with transaction.atomic():
            for day in Day.objects.all():
                diff_in_year = (day.year - day_zero.year)

                spring_datetime = Command.get_solarterm(day.year, u'입춘')

                if day.date < spring_datetime.time.date():
                    diff_in_year = (day.year - 1 - day_zero.year)

                zero_heaven_letter_index = ManseConstants.HEAVEN_LETTERS_INDEX[zero_heaven_letter] - 1
                zero_ground_letter_index = ManseConstants.GROUND_LETTERS_INDEX[zero_ground_letter] - 1

                mod10 = abs(diff_in_year) % 10
                mod12 = abs(diff_in_year) % 12

                mod10 = [mod10, -mod10][diff_in_year < 0]
                mod12 = [mod10, -mod12][diff_in_year < 0]

                heaven_index = (zero_heaven_letter_index + mod10) % 10
                ground_index = (zero_ground_letter_index + mod12) % 12

                day_heaven_letter = ManseConstants.HEAVEN_LETTERS[heaven_index]
                day_ground_letter = ManseConstants.GROUND_LETTERS[ground_index]

                # print day.year, diff_in_year, day_heaven_letter.encode('utf-8'), day_ground_letter.encode('utf-8')

                day.year_heaven_letter = day_heaven_letter
                day.year_ground_letter = day_ground_letter
                day.save()

    @classmethod
    def get_spring_jul_heaven_letter(cls, year):
        year_heaven_letter = Day.objects.get(year=year, month=6, day=1).year_heaven_letter
        spring_jul_heaven_letter = ManseConstants.YEAR_TO_SPRING_JUL_HEAVEN_LETTER_DICT[year_heaven_letter]
        return spring_jul_heaven_letter


