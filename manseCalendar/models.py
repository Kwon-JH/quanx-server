# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


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
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()

    year_heaven_letter = models.CharField(max_length=6)
    year_ground_letter = models.CharField(max_length=6)

    month_heaven_letter = models.CharField(max_length=6)
    month_heaven_letter = models.CharField(max_length=6)

    day_heaven_letter = models.CharField(max_length=6)
    day_heaven_letter = models.CharField(max_length=6)


class SolarTerm(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=6)
