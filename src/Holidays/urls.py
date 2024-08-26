from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from Holidays import views

from Holidays.views import inicio

router = routers.DefaultRouter()
router.register(r'holidays', views.HolidayViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', inicio, name='inicio'),
    path('api-auth/', include('rest_framework.urls')),
]