from django.db import models
from django.contrib.auth.models import User
from money_transfer.models import MoneyTransferPlatform  

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(MoneyTransferPlatform, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.platform.name} - {self.account_number}"
