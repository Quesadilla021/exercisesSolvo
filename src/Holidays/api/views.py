from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from djgentelella.objectmanagement import AuthAllPermBaseObjectManagement
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import BasePermission

from Holidays.models import Holiday
from Holidays.api import serializers, filterset


class EquipmentManagementViewset(AuthAllPermBaseObjectManagement):
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

    quaryset = Holiday.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('code', 'name')
    filterset_class = filterset.HolidayFilter
    ordering_fields = ['name']
    ordering = ('name',)
    operation_type = ''