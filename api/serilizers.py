from rest_framework import serializers
from moneytransfer.models import MoneyTransferPlatform, UserAccount, Transaction


class MoneyTransferPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyTransferPlatform
        fields = ['id', 'name', 'description']


class UserAccountSerializer(serializers.ModelSerializer):
    platform = MoneyTransferPlatformSerializer(read_only=True)
    platform_id = serializers.PrimaryKeyRelatedField(
        queryset=MoneyTransferPlatform.objects.all(), source='platform', write_only=True
    )

    class Meta:
        model = UserAccount
        fields = ['id', 'user', 'platform', 'platform_id', 'account_number', 'balance', 'created_at']
        read_only_fields = ['user', 'balance', 'created_at']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'transaction_type', 'amount', 'description', 'timestamp']
        read_only_fields = ['timestamp']
