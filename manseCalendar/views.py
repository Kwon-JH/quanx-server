from django.shortcuts import render
from rest_framework import generics
from .models import Day
from .serializers import DaySerializer


class APIConstants:
    YEAR = 'year'
    MONTH = 'month'
    DAY = 'day'
    IS_LUNAR_DATE = 'is_lunar_date'
    IS_LUNAR_LEAP_MONTH = 'is_lunar_leap_month'

    TRUE = '1'


# Create your views here.
class DayAPIView(generics.RetrieveAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    # lookup_field = None
    # lookup_url_kwarg = []

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        year = self.kwargs[APIConstants.YEAR]
        month = self.kwargs[APIConstants.MONTH]
        day = self.kwargs[APIConstants.DAY]

        if APIConstants.IS_LUNAR_DATE in self.kwargs:
            is_lunar_date = self.kwargs[APIConstants.IS_LUNAR_DATE] == APIConstants.TRUE
        else:
            is_lunar_date = False

        if is_lunar_date:
            is_lunar_leap_month = self.kwargs[APIConstants.IS_LUNAR_LEAP_MONTH] == APIConstants.TRUE

            filter_kwargs = {
                'lunar_year': year,
                'lunar_month': month,
                'lunar_day': day,
                'is_lunar_leap_month': is_lunar_leap_month
            }

        else:
            filter_kwargs = {
                'year': year,
                'month': month,
                'day': day,
            }

        obj = generics.get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj
