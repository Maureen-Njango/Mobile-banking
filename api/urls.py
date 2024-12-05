from django.urls import path
from .views import (
    MoneyTransferPlatformListView,
    UserAccountListView,
    TransactionListView,
    AccountDetailView,
)

urlpatterns = [
    path('moneytransfer/', MoneyTransferPlatformListView.as_view(), name='platforms'),
    path('accounts/', UserAccountListView.as_view(), name='accounts'),
    path('accounts/<int:account_id>/transactions/', TransactionListView.as_view(), name='transactions'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
]
