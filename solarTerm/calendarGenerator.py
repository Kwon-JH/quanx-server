#!/usr/bin/env python
# -*- coding: utf-8 -*-


# run code below in django shell

import datetime
import pandas as pd
from manseCalendar.models import SolarTerm, Day

df = pd.read_json('solarTerm_1800-2100.json')
for index, row in df.iterrows():
    t = datetime.datetime(row['year'], row['month'], row['day'], row['hour'], row['minute'])
    term = SolarTerm(time=t, name=row['name']);
    term.save()


start_date = datetime.datetime(1800, 1, 1)
end_date = datetime.datetime(2100,12,31)


a_day_datetime = datetime.datetime(1984, 6, 8)
a_day_object = Day(year=a_day_datetime.year, month=a_day_datetime.month, day=a_day_datetime.day,
                   year_heaven_letter='甲',
                   year_ground_letter='子',
                   month_heaven_letter='庚',
                   month_ground_letter='午',
                   day_heaven_letter='癸',
                   day_ground_letter='酉')


cur_date_time = datetime.datetime(1800, 1, 1)
while cur_date_time <= end_date:


    a_day_datetime += datetime.timedelta(days=1)
