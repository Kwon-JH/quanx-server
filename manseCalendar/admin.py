from django.contrib import admin

# Register your models here.
from manseCalendar.models import SolarTerm, Day


class SolarTermAdmin(admin.ModelAdmin):
    list_display = ('time', 'name', 'month_heaven_letter', 'month_ground_letter')

admin.site.register(SolarTerm, SolarTermAdmin)
# admin.site.register(SolarTerm)


class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'is_solar_term',
                    'year_heaven_letter', 'year_ground_letter',
                    'month_heaven_letter', 'month_ground_letter',
                    'day_heaven_letter', 'day_ground_letter',
                    'lunar_year', 'lunar_month', 'lunar_day', 'is_lunar_leap_month'
                    )

admin.site.register(Day, DayAdmin)