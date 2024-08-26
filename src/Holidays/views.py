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
    return render(request, 'Holidays/index.html')

logger = logging.getLogger(__name__)

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

class HolidayListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info("Fetching holidays")
        country = request.query_params.get('country', 'CR')
        name = request.query_params.get('name', '')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        try:
            holidays = Holiday.objects.filter(
                country=country,
                name__icontains=name,
                date__range=[start_date, end_date]
            )
            serializer = HolidaySerializer(holidays, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def fetch_holidays_from_api(year, country_code):
    url = f"https://date.nager.at/api/v2/publicholidays/{year}/{country_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


