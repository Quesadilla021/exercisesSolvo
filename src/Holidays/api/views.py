from django_filters.rest_framework import DjangoFilterBackend
from djgentelella.objectmanagement import AuthAllPermBaseObjectManagement
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import BasePermission

from Holidays.models import Holiday
from Holidays.api import serializers, filterset


class HolidayManagementViewset(AuthAllPermBaseObjectManagement):
    serializer_class = {
        'list':serializers.HolidayDataTableSerializer,
        'destroy':serializers.HolidaySerializer,
        'create':serializers.HolidaySerializer,
        'update':serializers.HolidaySerializer,
    }
    perms = {
        'list' : [],
        'destroy': [],
        'create': [],
        'update': [],
    }

    permission_classes = (BasePermission,)

    queryset = Holiday.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ['name', 'weekday', 'country']
    filterset_class = filterset.HolidayFilter
    ordering_fields = ['name']
    ordering = ('name',)
