from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from Holidays import views
from Holidays.api.views import HolidayManagementViewset

from Holidays.views import inicio, holiday_list

app_name = 'holidays'

router = routers.DefaultRouter()
router.register(r'holidays', views.HolidayViewSet)

objectrouter = DefaultRouter()
objectrouter.register("api_holiday_list", HolidayManagementViewset, basename="api-holiday")

urlpatterns = [
    path('api/', include(objectrouter.urls)),
    path('days/', inicio, name='home'),
    path('holidaylist/', holiday_list, name='holiday_list'),
    path('api-auth/', include('rest_framework.urls')),
]