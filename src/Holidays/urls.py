from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from Holidays import views
from Holidays.api.views import EquipmentManagementViewset

from Holidays.views import inicio

router = routers.DefaultRouter()
router.register(r'holidays', views.HolidayViewSet)

objectrouter = DefaultRouter()
objectrouter.register("api_holiday_list", EquipmentManagementViewset, basename="api-holiday")

urlpatterns = [
    path('', include(router.urls)),
    path('days/', inicio, name='inicio'),
    path('api-auth/', include('rest_framework.urls')),
]