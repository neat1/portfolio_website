from django.db import models
from django.db.models import Avg, Count, Sum
from django.contrib.auth.models import User


# Create your models here.
class Coin(models.Model):
    """Model representing an cryptocurrency."""
    ticker = models.CharField(max_length=200, unique=True, help_text='Look up the ticker manually now')
    name = models.CharField(max_length=200, help_text='Enter a cryptocurrency name (e.g. Bitcoin)')

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    """Model representing an individial portfolio."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200, help_text='Enter a portfolio name (e.g. Andras portfolio')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def total_portfolio_value(self):
        return sum([transaction.total_trade_value for transaction in self.transaction_set.all()])
    

class Transaction(models.Model):
    """Model representing a trade."""
    portfolio = models.ForeignKey('Portfolio',on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin,on_delete=models.CASCADE)
    number_of_coins = models.DecimalField(max_digits=10, decimal_places=0)
    trade_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return str(self.portfolio)   

    @property
    def total_trade_value(self):
        return self.trade_price * self.number_of_coins

    @property
    def transaction_ticker(self):
        return self.coin.ticker
      

class PortfolioView(models.Model):
    coin = models.OneToOneField(Coin,on_delete=models.CASCADE,primary_key=True)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE, default='SOME STRING')

    @property
    def distinct_coin(self):
       return  self.coin.ticker
    
