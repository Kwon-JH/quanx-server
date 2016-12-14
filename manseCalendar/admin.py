from django.contrib import admin

# Register your models here.
from manseCalendar.models import SolarTerm


class SolarTermAdmin(admin.ModelAdmin):
    list_display = ('time', 'name')

admin.site.register(SolarTerm, SolarTermAdmin)