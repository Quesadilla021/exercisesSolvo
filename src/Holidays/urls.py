from django.urls import path, include
from rest_framework.authtoken import views

from Holidays.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]