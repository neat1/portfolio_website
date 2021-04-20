from django.db import models
from django.db.models import Avg, Count, Sum
import uuid

# Create your models here.
class Security(models.Model):
    """Model representing an individial security"""
    cutip = models.IntegerField(primary_key=True, unique=True,)
    ticker = models.CharField(max_length=200, unique=True, help_text='Look up the ticker manually now')
    name = models.CharField(max_length=200, help_text='Enter a cryptocurrency name (e.g. Bitcoin)')

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    """Model representing an individial portfolio."""
    portfolio_id = models.IntegerField(primary_key=True, unique=True,auto_created=True,editable=False,)
    name = models.CharField(max_length=200, help_text='Enter a portfolio name (e.g. Andras portfolio') 

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    """maybe useful later"""
    @property
    def average_trade_price(self):
        return Trade.objects.all().aggregate(Avg('trade_price'))
    
    """maybe useful later"""
    @property
    def number_of_distinct_cutips(self):
        return Trade.objects.all().aggregate(Count('cutip',distinct=True))

    @property
    def total_porfolio_value(self):
        return sum([trade.total_trade_value for trade in self.trade_set.all()])

    @property
    def total_coin_value(self):
        return ([trade.total_trade_value for trade in self.trade_set.all().filter(portfolio_id=1)])
        

            
class Trade(models.Model):
    """Model representing a Cryptocurrency."""
    trade_id = models.IntegerField(primary_key=True, unique=True,auto_created=True,editable=False,)
    portfolio_id = models.ForeignKey('Portfolio',on_delete=models.CASCADE)
    cutip = models.ForeignKey(Security,on_delete=models.CASCADE)
    number_of_coins = models.DecimalField(max_digits=10, decimal_places=0)
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    

    class Meta:
        ordering = ['-date']
    
     
    def __str__(self):
        return str(self.trade_id)   

    @property
    def total_trade_value(self):
        return self.trade_price * self.number_of_coins