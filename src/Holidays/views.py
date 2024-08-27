import logging
import requests

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Holidays.models import Holiday
from Holidays.serializers import HolidaySerializer
from rest_framework import status
from rest_framework import viewsets

def inicio(request):
    holidays = Holiday.objects.all()
    return render(request, 'Holidays/index.html', {'holidays': holidays})

def holiday_list(request):
    form = ""
    return render(request, 'Holidays/crud.html', {'create_form': form})

#logger = logging.getLogger(__name__)

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer


