from django_filters.rest_framework import FilterSet

from Holidays.models import Holiday


class HolidayFilter(FilterSet):
    class Meta:
        model = Holiday
        fields = {'id': ['exact'],
                  'name': ['icontains'],
                  'weekday': ['icontains'],
                  'country': ['icontains'],

                  }