# -*- coding: utf-8 -*-

import codecs
import datetime

from django.core.management import BaseCommand

from manseCalendar.models import Day, SolarTerm


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--input', action='store', dest='input', help='calendar data file path', required=True)

    def handle(self, *args, **options):
        # Command.insert_days(options)
        Command.insert_solarterm_characters()

    @classmethod
    def insert_solarterm_characters(cls):
        zero_heaven_letter = u'庚'
        zero_ground_letter = u'午'

        day_zero = datetime.datetime.combine(datetime.date(1984, 6, 5), datetime.time.min)
        id = day = SolarTerm.objects.filter(time__gte=day_zero)[0]


    @classmethod
    def insert_days(cls, options):
        input_file_path = options['input']
        with codecs.open(input_file_path, 'r', encoding='utf8') as input:
            for line in input:
                solar, lunar = line.rstrip('\n').split('\t')

                # year, month, day = [ int(s.strip(u'년월일')) for s in solar.lstrip(u"양력").split()]
                year, month, day = solar.lstrip(u"양력").split()
                year = int(year.rstrip(u'년'))
                month = int(month.rstrip(u'월'))
                day = int(day.rstrip(u'일'))

                solar_date = datetime.datetime(year, month, day)

                lunar_year, lunar_month, lunar_day, lunar_month_kind = lunar.lstrip(u"음력").split()
                lunar_year = int(lunar_year.rstrip(u'년'))
                lunar_month = int(lunar_month.rstrip(u'월'))
                lunar_day = int(lunar_day.rstrip(u'일'))
                lunar_month_kind = lunar_month_kind.strip('() ')

                is_lunar_leap_month = lunar_month_kind == u'윤달'

                # if is_lunar_leap_month:
                #     print solar_date, lunar.encode('utf-8')
                day = Day(year=year,
                          month=month,
                          day=day,
                          date=solar_date,
                          lunar_year=lunar_year,
                          lunar_month=lunar_month,
                          lunar_day=lunar_day,
                          is_lunar_leap_month=is_lunar_leap_month
                          )

                day.save()