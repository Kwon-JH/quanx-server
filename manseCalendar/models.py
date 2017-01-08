# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models


# Create your models here.

['소한', '입춘', '경칩', '청명', '입하', '망종', '소서', '입추', '백로', '한로', '입동', '대설']

class ManseConstants:
    HEAVEN_LETTERS = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    GROUND_LETTERS = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    SIXTY_LETTERS = ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥',
                     '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥',
                     '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥',
                     '庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥',
                     '壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']

    HEAVEN_LETTERS_INDEX = {'甲': 1, '乙': 2, '丙': 3, '丁': 4, '戊': 5,
                            '己': 6, '庚': 7, '辛': 8, '壬': 9, '癸': 10}

    GROUND_LETTERS_INDEX = {'子': 1, '丑': 2, '寅': 3, '卯': 4, '辰': 5,
                            '巳': 6, '午': 7, '未': 8, '申': 9, '酉': 10, '戌': 11, '亥': 12}


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


class SolarTerm(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=6)

    month_heaven_letter = models.CharField(max_length=6, null=True)
    month_ground_letter = models.CharField(max_length=6, null=True)
