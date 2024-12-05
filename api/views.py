from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from moneytransfer.models import MoneyTransferPlatform, UserAccount, Transaction
from .serializers import MoneyTransferPlatformSerializer, UserAccountSerializer, TransactionSerializer


class MoneyTransferPlatformListView(ListCreateAPIView):
    queryset = MoneyTransferPlatform.objects.all()
    serializer_class = MoneyTransferPlatformSerializer
    permission_classes = [IsAuthenticated]


class UserAccountListView(ListCreateAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionListView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return Transaction.objects.filter(account__id=account_id, account__user=self.request.user)

    def perform_create(self, serializer):
        account = UserAccount.objects.get(id=self.kwargs['account_id'], user=self.request.user)
        serializer.save(account=account)


class AccountDetailView(RetrieveAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserAccount.objects.filter(user=self.request.user)
