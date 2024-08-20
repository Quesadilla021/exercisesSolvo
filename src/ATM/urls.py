from django.urls import path

from ATM.views import inicio, withdraw, account_list, account_create, account_update, account_delete, validate_account

urlpatterns = [
    path('', inicio, name='inicio'),
    path('withdraw/', withdraw, name='withdraw'),
    path('accounts/', account_list, name='account_list'),
    path('accounts/nuevo/', account_create, name='account_create'),
    path('accounts/editar/<int:pk>/', account_update, name='account_update'),
    path('accounts/eliminar/<int:pk>/', account_delete, name='account_delete'),
    path('validate_account/', validate_account, name='validate_account'),
]