from django.db import models
from .models import account

class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)  
    transaction_type = models.CharField(
        max_length=10,
        choices=[("credit", "Credit"), ("debit", "Debit")],  
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)  
    description = models.TextField(blank=True, null=True) 
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.account.account_number} - {self.transaction_type} - {self.amount}"
