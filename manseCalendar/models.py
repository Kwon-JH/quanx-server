# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models


# Create your models here.


class ManseConstants:
    HEAVEN_LETTERS = [u'甲', u'乙', u'丙', u'丁', u'戊', u'己', u'庚', u'辛', u'壬', u'癸']
    GROUND_LETTERS = [u'子', u'丑', u'寅', u'卯', u'辰', u'巳', u'午', u'未', u'申', u'酉', u'戌', u'亥']
    SIXTY_LETTERS = ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥',
                     '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥',
                     '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥',
                     '庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥',
                     '壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']

    HEAVEN_LETTERS_INDEX = {u'甲': 1, u'乙': 2, u'丙': 3, u'丁': 4, u'戊': 5,
                            u'己': 6, u'庚': 7, u'辛': 8, u'壬': 9, u'癸': 10}

    GROUND_LETTERS_INDEX = {u'子': 1, u'丑': 2, u'寅': 3, u'卯': 4, u'辰': 5, u'巳': 6,
                            u'午': 7, u'未': 8, u'申': 9, u'酉': 10, u'戌': 11, u'亥': 12}



    # JUL_INDEX = {'입춘': 1, '경칩': 2, '청명': 3, '입하': 4, '망종': 5, '소서': 6,
    #              '입추': 7, '백로': 8, '한로': 9, '입동': 10, '대설': 11, '소한': 12}
    #
    # JUL_LIST = ['입춘', '경칩', '청명', '입하', '망종', '소서',
    #             '입추', '백로', '한로', '입동', '대설', '소한']
    #
    # JULKI_INDEX = {'입춘': 1, '우수': 2, '경칩': 3, '춘분': 4, '청명': 5, '곡우': 6,
    #                '입하': 7, '소만': 8, '망종': 9, '하지': 10, '소서': 11, '대서': 12,
    #                '입추': 13, '처서': 14, '백로': 15, '추분': 16, '한로': 17, '상강': 18,
    #                '입동': 19, '소설': 20, '대설': 21, '동지': 22, '소한': 23, '대한': 24}

    JUL_LIST = ['소한', '입춘', '경칩', '청명', '입하', '망종',
                '소서', '입추', '백로', '한로', '입동', '대설']

    JUL_INDEX = {jul: index for index, jul in enumerate(JUL_LIST)}

    JULKI_LIST = ['소한', '대한', '입춘', '우수', '경칩', '춘분', '청명', '곡우',
                  '입하', '소만', '망종', '하지', '소서', '대서',
                  '입추', '처서', '백로', '추분', '한로', '상강',
                  '입동', '소설', '대설', '동지']

    JULKI_INDEX = {julki: index for index, julki in enumerate(JULKI_LIST)}

    YEAR_TO_SPRING_JUL_HEAVEN_LETTER_DICT = {'甲': u'丙', '乙': u'戊', '丙': u'庚', '丁': u'壬', '戊': u'甲',
                                 '己': u'丙', '庚': u'戊', '辛': u'庚', '壬': u'壬', '癸': u'甲'}


class Day(models.Model):
    id = models.AutoField(primary_key=True)

    year = models.PositiveSmallIntegerField(null=True)
    month = models.PositiveSmallIntegerField(null=True)
    day = models.PositiveSmallIntegerField(null=True)

    date = models.DateField(default=datetime.date.today)

    lunar_year = models.PositiveSmallIntegerField(null=True)
    lunar_month = models.PositiveSmallIntegerField(null=True)
    lunar_day = models.PositiveSmallIntegerField(null=True)

    is_lunar_leap_month = models.BooleanField(default=False)

    is_solar_term = models.BooleanField(default=False)

    year_heaven_letter = models.CharField(max_length=6, null=True)
    year_ground_letter = models.CharField(max_length=6, null=True)

    month_heaven_letter = models.CharField(max_length=6, null=True)
    month_ground_letter = models.CharField(max_length=6, null=True)

    day_heaven_letter = models.CharField(max_length=6, null=True)
    day_ground_letter = models.CharField(max_length=6, null=True)

    class Meta:
        ordering = ['date']


class SolarTerm(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=6)

    month_heaven_letter = models.CharField(max_length=6, null=True)
    month_ground_letter = models.CharField(max_length=6, null=True)

    class Meta:
        ordering = ['time']
