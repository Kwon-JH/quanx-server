from django.conf.urls import url, include
from .views import DayAPIView

urlpatterns = [
    url(r'^manse_calendar/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$',
        DayAPIView.as_view(),
        name='get_day'),
]
