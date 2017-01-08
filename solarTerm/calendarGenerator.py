#!/usr/bin/env python
# -*- coding: utf-8 -*-


# run code below in django shell

import datetime
import sys
import urllib
import urllib2

from concurrent.futures import ThreadPoolExecutor
from lxml.html import fromstring
from selenium import webdriver

['소한', '입춘', '경칩', '청명', '입하', '망종', '소서', '입추', '백로', '한로', '입동', '대설']


def create_day():

    # start_date = datetime.datetime(1800, 1, 1)
    end_date = datetime.datetime(2050, 12, 31)
    # end_date = datetime.datetime(1800, 1, 10)

    a_day = datetime.datetime(1800, 1, 1)

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(10)

    driver.get('https://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_daily_s2l.php')

    with open('lunar_date.txt', 'w') as output:
        while a_day <= end_date:

            input_year = driver.find_elements_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > input[type="text"]:nth-child(1)')[0]
            input_month = driver.find_elements_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > input[type="text"]:nth-child(3)')[0]
            input_day = driver.find_elements_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > input[type="text"]:nth-child(5)')[0]

            # button_submit = driver.find_element_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2) > input[type="image"]')

            year_string = str(a_day.year)
            month_string = str(a_day.month)
            day_string = str(a_day.day)

            input_year.send_keys(year_string)
            input_month.send_keys(month_string)
            input_day.send_keys(day_string)

            input_day.submit()

            td_lunar_date = driver.find_element_by_css_selector('#life > div.graybox_area2 > div > table > tbody > tr:nth-child(2) > td')
            td_leap_info = driver.find_element_by_css_selector('#life > div.graybox_area2 > div > table > tbody > tr:nth-child(5) > td')

            field_list = [td_lunar_date.text]
            field_list.extend(td_leap_info.text.split('\n'))

            output.write(u'\t'.join(field_list).encode('utf8'))
            output.write('\n\n')

            a_day += datetime.timedelta(days=31)

            output.flush()

    driver.close()


def get_lunar_date(year, month):
    start_date = datetime.datetime(year, month, 1)
    a_day = datetime.datetime(year, month, 1)
    end_date = datetime.datetime(year, month+1, 1)

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(10)

    driver.get('https://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_daily_s2l.php')

    filename = 'data/solar_to_lunar_%d-%02d.txt' % (a_day.year, a_day.month)
    with open(filename, 'w') as output:
        while a_day < end_date:

            input_year = driver.find_elements_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > input[type="text"]:nth-child(1)')[0]
            input_month = driver.find_elements_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > input[type="text"]:nth-child(3)')[0]
            input_day = driver.find_elements_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > input[type="text"]:nth-child(5)')[0]

            # button_submit = driver.find_element_by_css_selector('#life > div.graybox_area2 > div > form > div > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2) > input[type="image"]')

            year_string = str(a_day.year)
            month_string = str(a_day.month)
            day_string = str(a_day.day)

            input_year.send_keys(year_string)
            input_month.send_keys(month_string)
            input_day.send_keys(day_string)

            input_day.submit()

            td_lunar_date = driver.find_element_by_css_selector('#life > div.graybox_area2 > div > table > tbody > tr:nth-child(2) > td')
            # td_leap_info = driver.find_element_by_css_selector('#life > div.graybox_area2 > div > table > tbody > tr:nth-child(5) > td')


            # field_list = [td_lunar_date.text]
            # field_list.extend(td_leap_info.text.split('\n'))

            # output.write(u'\t'.join(field_list).encode('utf8'))
            # output.write('\n\n')

            solar_date_string = u'{year}년 {month}월 {day}일'.format(year=a_day.year, month=a_day.month, day=a_day.day)
            s = u'양력 {solar_date}\t음력 {lunar_date}\n'.format(solar_date=solar_date_string, lunar_date=td_lunar_date.text)
            output.write(s.encode('utf-8'))
            a_day += datetime.timedelta(days=1)

            # output.flush()
    driver.close()

NUMBER_OF_DAYS_IN_A_MONTH = [31, 28, 31, 30, 31, 30,
                             31, 31, 30, 31, 30, 31]


def lines(file_descriptor):
    for line in file_descriptor:
        yield line


def count_line(file_path):
    number_of_line = 0
    try:
        with open(file_path, 'r') as input:
            for line in input:
                number_of_line += 1
    except IOError as e:
        sys.stderr.write(str(e))
        number_of_line = 0

    return number_of_line


def get_lunar_date_using_urllib_lxml(year, month):
    start_date = datetime.datetime(year, month, 1)


    if month == 12:
        end_date = datetime.datetime(year + 1, 1, 1)
    else:
        end_date = datetime.datetime(year, month + 1, 1)

    url = 'https://astro.kasi.re.kr/Life/Knowledge/solar2lunar/convert_daily_s2l.php'

    output_file_path = 'data/solar_to_lunar_%d-%02d.txt' % (year, month)

    line_count = count_line(output_file_path)
    if line_count >= NUMBER_OF_DAYS_IN_A_MONTH[month - 1]:
        return

    mode = 'a'
    if line_count == 0:
        mode = 'w'

    a_day = datetime.datetime(year, month, line_count + 1)

    with open(output_file_path, mode) as output:
        while a_day < end_date:
            # sol_year = 2016 & sol_month = 12 & sol_day = 31 & x = 0 & y = 0
            values = {'sol_year': a_day.year,
                      'sol_month': a_day.month,
                      'sol_day': a_day.day,
                      'x': 0,
                      'y': 0}

            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
            h = fromstring(the_page.decode('euc-kr'))
            selector_string = '#life > div.graybox_area2 > div > table > tr > td '

            result_list = h.cssselect(selector_string)

            solar_date_string = u'{year}년 {month}월 {day}일'.format(year=a_day.year, month=a_day.month, day=a_day.day)
            lunar_date_string = result_list[0].text_content()
            line = u'양력 {solar_date}\t음력 {lunar_date}\n'.format(solar_date=solar_date_string,
                                                                lunar_date=lunar_date_string)

            output.write(line.encode('utf-8'))
            output.flush()
            a_day += datetime.timedelta(days=1)



def solar_to_lunar():
    # start_date = datetime.datetime(1800, 1, 1)
    # end_date = datetime.datetime(2050, 12, 31)
    # end_date = datetime.datetime(1800, 1, 10)

    # a_day = datetime.datetime(1885, 1, 1)

    with ThreadPoolExecutor(max_workers=12) as executor:
        for year in range(1800, 2051) :
            for month in range(1, 13):
                # print (year, month)
                executor.submit(get_lunar_date_using_urllib_lxml, year, month)
        # while a_day < end_date:
        #     for month in range(1, 13):
        #     year = a_day.year
        #     month = a_day.month
        #
        #     executor.submit(get_lunar_date_using_urllib_lxml, year, month)
        #     a_day += datetime.timedelta(days=31)
        #     a_day.replace(day=1)

# def main():
#     input = FileStream('lunar_date.txt', encoding='utf-8')
#     lexer = lunarInformationLexer.lunarInformationLexer(input)
#     stream = CommonTokenStream(lexer)
#     parser = lunarInformationParser.lunarInformationParser(stream)
#     tree = parser.lunarDate()
#     print(tree.toStringTree(recog=parser))
#
#
#     listener = lunarInformationListener()
#     walker = ParseTreeWalker()
#     walker.walk(listener, tree)

# if __name__ == '__main__':
#     main()

def merge_output():
    with open('solar_to_lunar_date_1800-2051.txt', 'w') as merged_file:
        for year in range(1800, 2051):
            for month in range(1, 13):
                output_file_path = 'data/solar_to_lunar_%d-%02d.txt' % (year, month)
                with open(output_file_path, 'r') as input:
                    for line in input:
                        merged_file.write(line)
                        # merged_file.write('\n')


if __name__ == '__main__':
    merge_output()
    # solar_to_lunar()
    # get_lunar_date_using_urllib_lxml(2031,11)
#
#

# a_day_datetime = datetime.datetime(1984, 6, 8)
# a_day_object = Day(year=a_day_datetime.year, month=a_day_datetime.month, day=a_day_datetime.day,
#                    year_heaven_letter='甲',
#                    year_ground_letter='子',
#                    month_heaven_letter='庚',
#                    month_ground_letter='午',
#                    day_heaven_letter='癸',
#                    day_ground_letter='酉')
#
#
# cur_date_time = datetime.datetime(1800, 1, 1)
# while cur_date_time <= end_date:
#
#
#     a_day_datetime += datetime.timedelta(days=1)
