from django.db import models
from django.db.models import Avg, Count, Sum
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
    """Model representing an individial portfolio"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200, help_text='Enter a portfolio name (e.g. Andras portfolio)')

    def __str__(self):
        return str(self.name)

    def nos(self):
        """return Transaction.objects.all()"""
        valami =  Transaction.objects.all()
        
        
    
class Coin(models.Model):
    """Model representing an individial security"""
    ticker = models.CharField(max_length=200, unique=True, help_text='Look up the ticker manually now')
    name = models.CharField(max_length=200, help_text='Enter a cryptocurrency name (e.g. Bitcoin)')
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return str(self.name)

    def number_bought(Self):
        return Transaction.objects.all().aggregate(Count('number_of_coins',distinct=True))

class Transaction(models.Model):
    stock = models.ForeignKey('Coin',on_delete=models.CASCADE)
    number_of_coins = models.DecimalField(max_digits=10, decimal_places=0)
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return str(self.stock)

    @property
    def total_trade_value(self):
        return self.trade_price * self.number_of_coins
    
    
    
   
