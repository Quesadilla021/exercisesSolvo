import logging
import requests

from django.shortcuts import render

from Holidays.forms import HolidayForm
from Holidays.models import Holiday
from Holidays.serializers import HolidaySerializer
from rest_framework import viewsets

def inicio(request):
    holidays = Holiday.objects.all()
    return render(request, 'Holidays/index.html', {'holidays': holidays})

def holiday_list(request):
    form_creacion = HolidayForm(prefix="create", modal_id="create_obj_modal")
    form_actualizacion = HolidayForm(prefix="update", modal_id="update_obj_modal")
    return render(request, 'Holidays/index.html', {'create_form': form_creacion, 'update_form': form_actualizacion})

#logger = logging.getLogger(__name__)

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer


