from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    CONSERVATIVE = "CS"
    MODERATE = "MD"
    BOLD = "BD"
    RISK_CHOICES = [ 
        (CONSERVATIVE, 'Conservador'),
        (MODERATE,'Moderado'),
        (BOLD,'Arrojado')
    ]

    email = models.CharField(max_length=20)
    username = models.CharField(max_length=50)    
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    risk_person = models.CharField(max_length=2,choices=RISK_CHOICES, default=CONSERVATIVE)
    
class Operacao (models.Model):  
    amount = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    trading_value = models.DecimalField(max_digits=6,decimal_places=2,default=0) 
    purchase_value = models.DecimalField(max_digits=6,decimal_places=2,default=0) 
    tax = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    totalOperationValue = models.DecimalField(max_digits=6,decimal_places=2,default=0)

    shareName = models.CharField(max_length=10,default="EMPRESA") 
    type_operation = models.CharField(max_length=2,default="N")
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Investor,on_delete=models.CASCADE)
    
    